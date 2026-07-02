import logging

from faker import Faker

from config.settings import (
    METADATA_JSON,
    TEST_RAW_CSV,
    TEST_SYNTHETIC_CSV,
    setup_logger,
)
from scripts.data_utils.generator_core import run_sdv_generation

# パス設定
INPUT_PATH = TEST_RAW_CSV
OUTPUT_PATH = TEST_SYNTHETIC_CSV

# ログ設定
setup_logger()
logger = logging.getLogger(__name__)

faker_jp = Faker("ja_JP")


def add_dummy_info(df):
    num_row = len(df)
    df["id"] = range(1, num_row + 1)
    df["customer_code"] = [f"USR-{10000 + i}" for i in range(num_row)]
    df["customer_name"] = [faker_jp.name() for _ in range(num_row)]

    # 追加列を左端に配置
    cols = ["id", "customer_code", "customer_name"] + [
        c for c in df.columns if c not in ["id", "customer_code", "customer_name"]
    ]
    return df[cols]  # 新しいDFを返す


def main():
    # 共通の生成処理の呼び出し
    logger.info("WEBアプリ用疑似データを生成します")
    synthetic_data = run_sdv_generation(INPUT_PATH, METADATA_JSON, is_training=False)

    # アプリ用データの加工
    logger.info("ダミー情報を付与しています")
    app_data = add_dummy_info(synthetic_data)

    # 保存
    app_data.to_csv(OUTPUT_PATH, index=False)
    logger.info(f"データ生成が完了しました: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
