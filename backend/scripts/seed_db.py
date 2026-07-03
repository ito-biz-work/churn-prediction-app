import logging

import pandas as pd

from backend.app.database import engine
from backend.app.models.customer_metrics import Base
from config.settings import TABLE_NAME, TEST_SYNTHETIC_CSV, setup_logger

# ログ設定
setup_logger()
logger = logging.getLogger(__name__)


def import_csv_to_db():
    """CSVファイルを読み込み、データベースのテーブルへ取り込む"""
    INPUT_PATH = TEST_SYNTHETIC_CSV

    # 読み込み
    df = pd.read_csv(INPUT_PATH)

    # 書き込み
    # Pandasのindexを除外
    df.to_sql(TABLE_NAME, con=engine, if_exists="append", index=False)

    logger.info(f"成功: {len(df)} 件のデータをデータベースにインポートしました")


if __name__ == "__main__":
    # テーブルの削除・作成
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # 初期データ投入
    import_csv_to_db()

    logger.info("データベースを初期化しました")
