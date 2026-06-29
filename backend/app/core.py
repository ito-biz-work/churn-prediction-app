from functools import lru_cache

import joblib
import pandas as pd
from sqlalchemy.orm import Session

from backend.app.models.customer_metrics import CustomerMetrics
from backend.app.schemas import PredictionInput, PredictionOutput
from config.settings import MODEL_JOBLIB


@lru_cache(maxsize=1)
def get_model():
    """初回のみ実行、2回目以降はキャッシュを返却"""
    return joblib.load(MODEL_JOBLIB)


def get_prediction(data: PredictionInput) -> PredictionOutput:
    """機械学習モデルによる退会確率の予測結果を返す"""

    # Pydanticモデルを推論可能な形式(DataFrame)に変換
    df = pd.DataFrame([data.model_dump()])

    # モデルを取得
    model = get_model()

    # 推論の実行
    churn_index = list(model.classes_).index(1)  # 「1:yes」のラベル位置を特定
    probability = float(model.predict_proba(df)[0][churn_index])

    return PredictionOutput(probability=probability)


def get_customers(db: Session, skip: int = 0, limit: int = 5):
    """指定した範囲の顧客データと総件数を取得する"""
    total_count = db.query(CustomerMetrics).count()
    target_customers = db.query(CustomerMetrics).offset(skip).limit(limit).all()
    return {"total_count": total_count, "items": target_customers}
