from fastapi import APIRouter

from backend.app.core import get_prediction
from backend.app.schemas import PredictionInput, PredictionOutput

router = APIRouter()


@router.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    return get_prediction(input_data)
