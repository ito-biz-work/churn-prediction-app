from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.app.crud import check_db_health, get_customers
from backend.app.database import get_db
from backend.app.prediction import get_prediction
from backend.app.schemas import CustomerListOutput, PredictionInput, PredictionOutput

router = APIRouter()


@router.post("/predict", response_model=PredictionOutput, tags=["Prediction"])
def predict(data: PredictionInput):
    """退会確率を予測"""
    return get_prediction(data)


@router.get("/customers", response_model=CustomerListOutput, tags=["Customers"])
def list_customers(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0, description="スキップする件数"),
    limit: int = Query(5, gt=0, description="取得する件数"),
):
    """指定した範囲の顧客データと総件数を取得する"""
    return get_customers(db, skip=skip, limit=limit)


@router.get("/health", tags=["System"])
def health_check(db: Session = Depends(get_db)):
    """データベースの生存確認を含めたヘルスチェック"""
    check_db_health(db)
    return {"status": "ok"}
