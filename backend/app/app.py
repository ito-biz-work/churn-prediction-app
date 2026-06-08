from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core import get_customers, get_prediction
from backend.app.database import get_db
from backend.app.schemas import CustomerListOutput, PredictionInput, PredictionOutput

router = APIRouter()


@router.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    return get_prediction(input_data)


@router.get("/customers", response_model=list[CustomerListOutput])
def list_customers(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return get_customers(db, skip=skip, limit=limit)
