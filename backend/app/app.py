from fastapi import APIRouter

from .core import get_prediction
from .schemas import PredictionInput, PredictionOutput

router = APIRouter()


@router.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    return get_prediction(input_data)
