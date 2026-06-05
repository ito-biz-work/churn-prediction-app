import pandas as pd

from backend.app.database import engine
from backend.app.models.customer_metrics import Base
from config.settings import SYNTHETIC_DATA_DIR


def import_csv_to_db():
    """CSVファイルを読み込み、データベースのテーブルへ取り込む"""
    CSV_PATH = SYNTHETIC_DATA_DIR / "app.csv"

    # 読み込み
    df = pd.read_csv(CSV_PATH)

    # 書き込み
    # Pandasのindexを除外し、DB側のidカラムを自動採番
    df.to_sql("customer_metrics", con=engine, if_exists="replace", index=False)

    print(f"成功: {len(df)} 件のデータをデータベースにインポートしました。")


if __name__ == "__main__":
    # テーブルの作成（まだ存在しない場合のみ）
    Base.metadata.create_all(bind=engine)

    import_csv_to_db()
