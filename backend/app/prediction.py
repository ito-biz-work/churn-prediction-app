from functools import lru_cache

import joblib
import pandas as pd

from backend.app.schemas import PredictionInput, PredictionOutput
from config.settings import MODEL_JOBLIB


@lru_cache(maxsize=1)
def get_pipeline():
    """初回のみ実行、2回目以降はキャッシュを返却"""
    return joblib.load(MODEL_JOBLIB)


def predict_churn_probability(df: pd.DataFrame) -> list[float]:
    """【共通ロジック】複数件・1件兼用の推論処理"""
    pipe = get_pipeline()
    churn_index = list(pipe.classes_).index(1)  # 「1:yes」のラベル位置を特定
    probabilities = pipe.predict_proba(df)[:, churn_index]
    return [float(p) for p in probabilities]


def get_prediction(data: PredictionInput) -> PredictionOutput:
    """API用の1件の退会確率予測"""
    # Pydanticモデルを推論可能な形式(DataFrame)に変換
    df = pd.DataFrame([data.model_dump()])
    probabilities = predict_churn_probability(df)
    return PredictionOutput(probability=probabilities[0])
