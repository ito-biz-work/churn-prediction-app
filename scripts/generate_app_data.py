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
    df["customer_name"] = [faker_jp.name() for _ in range(num_row)]

    head = ["customer_name"]
    others = [c for c in df.columns if c not in head]

    # 追加列を左端に配置した新しいDFを返す
    return df[head + others]


def main():
    # 共通の生成処理の呼び出し
    logger.info("WEBアプリ用疑似データを生成します")
    synthetic_data = run_sdv_generation(INPUT_PATH, METADATA_JSON, is_training=False)

    # アプリ用データの加工
    logger.info("ダミー情報を付与しています")
    app_data = add_dummy_info(synthetic_data)

    # 保存
    app_data.to_csv(OUTPUT_PATH, index=False)
    logger.info(f"WEBアプリ用疑似データ生成が完了しました: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
