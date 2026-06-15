from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.app.core import get_customers, get_prediction
from backend.app.database import get_db
from backend.app.schemas import CustomerListOutput, PredictionInput, PredictionOutput

router = APIRouter()


@router.post("/predict", response_model=PredictionOutput, tags=["Prediction"])
def predict(data: PredictionInput):
    return get_prediction(data)


@router.get("/customers", response_model=CustomerListOutput, tags=["Customers"])
def list_customers(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="スキップする件数"),
    limit: int = Query(5, gt=0, description="取得する件数"),
):
    return get_customers(db, skip=skip, limit=limit)
