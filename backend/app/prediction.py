import logging
import os
import tempfile

import boto3
import joblib
import pandas as pd
from fastapi import Request

from backend.app.schemas import PredictionInput, PredictionOutput
from config.settings import ML_MODEL_NAME, MODEL_JOBLIB, setup_logger

# ログ設定
setup_logger()
logger = logging.getLogger(__name__)


def load_pipeline():
    """S3またはローカルからモデルをロードしてオブジェクトとして返す"""
    s3_bucket = os.getenv("S3_BUCKET_NAME")
    s3_key = ML_MODEL_NAME

    if s3_bucket:
        logger.info(f"S3からモデルをダウンロード: s3://{s3_bucket}/{s3_key}")
        s3_client = boto3.client("s3")
        temp_dir = tempfile.gettempdir()
        local_model_path = os.path.join(temp_dir, "downloaded_model.joblib")
        s3_client.download_file(s3_bucket, s3_key, local_model_path)
        return joblib.load(local_model_path)
    else:
        logger.info(f"ローカルからモデルをロード: {MODEL_JOBLIB}")
        return joblib.load(MODEL_JOBLIB)


def get_pipeline(request: Request):
    """app.state から pipeline を取り出すヘルパー関数"""
    return request.app.state.pipeline


def predict_churn_probability(df: pd.DataFrame, pipe) -> list[float]:
    """【共通ロジック】複数件・1件兼用の推論処理"""
    churn_index = list(pipe.classes_).index(1)  # 「1:yes」のラベル位置を特定
    probabilities = pipe.predict_proba(df)[:, churn_index]
    return [float(p) for p in probabilities]


def get_prediction(data: PredictionInput, pipe) -> PredictionOutput:
    """API用の1件の退会確率予測"""
    # Pydanticモデルを推論可能な形式(DataFrame)に変換
    df = pd.DataFrame([data.model_dump()])
    probabilities = predict_churn_probability(df, pipe)
    return PredictionOutput(probability=probabilities[0])
