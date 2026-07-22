import logging
from contextlib import closing

import pandas as pd
from pydantic import TypeAdapter
from sqlalchemy import update

from backend.app.database import SessionLocal, engine
from backend.app.models.customer_metrics import CustomerMetrics
from backend.app.prediction import load_pipeline, predict_churn_probability
from backend.app.schemas import PredictionInput
from config.settings import setup_logger

# ログ設定
setup_logger()
logger = logging.getLogger(__name__)


def bulk_predict():
    """DB内の顧客データを全件取得し、一括で退会予測を行って結果を更新する"""
    logger.info("一括予測処理を開始します")

    try:
        with closing(SessionLocal()) as db:
            # 顧客データを全件取得
            query = db.query(CustomerMetrics).statement
            df = pd.read_sql_query(query, engine)

        if df.empty:
            logger.info("予測対象の顧客データが存在しません")
            return

        logger.info(f"ターゲットデータ取得完了: {len(df)} 件")

        # PandasのデータをPydanticが読める形式（辞書のリスト）に変換
        raw_records = df.to_dict(orient="records")

        # Pydanticスキーマで一括バリデーション（不要なカラムは自動除去）
        adapter = TypeAdapter(list[PredictionInput])
        validated_records = adapter.validate_python(raw_records)

        # 綺麗になったデータを、再びモデルが読めるPandasの形式（DataFrame）に戻す
        X_predict = pd.DataFrame(
            [r.model_dump(by_alias=False) for r in validated_records]
        )

        # 一括予測
        pipe = load_pipeline()  # モデルをロード（S3/ローカル）
        probabilities = predict_churn_probability(X_predict, pipe)

        # 一括更新
        df["churn_probability"] = probabilities
        update_data = df[["id", "churn_probability"]].to_dict(orient="records")

        with closing(SessionLocal()) as db:
            db.execute(update(CustomerMetrics), update_data)
            db.commit()

        logger.info("一括予測処理が正常に終了しました")

    except Exception:
        logger.exception("一括予測処理中にエラーが発生しました")


if __name__ == "__main__":
    bulk_predict()
