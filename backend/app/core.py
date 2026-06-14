import joblib
import pandas as pd
from sqlalchemy.orm import Session

from backend.app.models.customer_metrics import CustomerMetrics
from backend.app.schemas import PredictionInput, PredictionOutput
from config.settings import MODEL_JOBLIB

# サーバー起動時に1回だけモデルをロード
model = joblib.load(MODEL_JOBLIB)


def get_prediction(data: PredictionInput) -> PredictionOutput:
    """機械学習モデルによる退会確率の予測結果を返す"""

    # Pydanticモデルを推論可能な形式(DataFrame)に変換
    df = pd.DataFrame([data.model_dump()])

    # 推論の実行
    # 「1:yes」のラベル位置を特定して確率を取得
    churn_index = list(model.classes_).index(1)
    probability = float(model.predict_proba(df)[0][churn_index])

    return PredictionOutput(probability=probability)


def get_customers(db: Session, skip: int = 0, limit: int = 5):
    total_count = db.query(CustomerMetrics).count()
    target_customers = db.query(CustomerMetrics).offset(skip).limit(limit).all()
    return {"total_count": total_count, "items": target_customers}
