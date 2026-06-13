import joblib
import pandas as pd
from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.app.models.customer_metrics import CustomerMetrics
from backend.app.schemas import PredictionInput, PredictionOutput
from config.settings import MODEL_JOBLIB

# サーバー起動時に1回だけモデルをロード
model = joblib.load(MODEL_JOBLIB)


def get_customer_prediction(customer_id: int, db: Session) -> PredictionOutput:
    # 顧客情報の取得
    customer = get_customer(customer_id, db)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # DBモデルから推論用入力データを生成
    data = PredictionInput.model_validate(customer)

    # 予測を実施
    prediction = get_prediction(data)

    return PredictionOutput(
        customer=customer,
        probability=prediction["probability"],
    )


def get_prediction(input_data: PredictionInput) -> float:
    """ "入力データを受け取り、モデルで推論して結果を返す"""
    # Pydanticモデルを辞書に変換し、PandasのDataFrameにする
    df = pd.DataFrame([input_data.model_dump()])

    # 推論
    churn_index = list(model.classes_).index(1)  # 「1:yes」のラベルを探す
    probability = float(model.predict_proba(df)[0][churn_index])  # 確率

    return {"probability": probability}


def get_customer(customer_id: int, db: Session):
    return db.query(CustomerMetrics).filter(CustomerMetrics.id == customer_id).first()


def get_customers(db: Session, skip: int = 0, limit: int = 5):
    total_count = db.query(CustomerMetrics).count()
    target_customers = db.query(CustomerMetrics).offset(skip).limit(limit).all()
    return {"total_count": total_count, "items": target_customers}
