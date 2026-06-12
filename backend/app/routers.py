from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.app.core import get_customer_prediction, get_customers
from backend.app.database import get_db
from backend.app.schemas import CustomerListOutput, PredictionOutput

router = APIRouter()


@router.post("/predict", response_model=PredictionOutput, tags=["Prediction"])
def predict(customer_id: int, db: Session = Depends(get_db)):
    return get_customer_prediction(customer_id, db)


@router.get("/customers", response_model=CustomerListOutput, tags=["Customers"])
def list_customers(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="スキップする件数"),
    limit: int = Query(5, gt=0, description="取得する件数"),
):
    return get_customers(db, skip=skip, limit=limit)
