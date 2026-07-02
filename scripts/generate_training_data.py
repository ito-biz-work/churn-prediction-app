import logging

from config.settings import (
    METADATA_JSON,
    TRAIN_RAW_CSV,
    TRAIN_SYNTHETIC_CSV,
    setup_logger,
)
from scripts.data_utils.generator_core import run_sdv_generation

# パス設定
INPUT_PATH = TRAIN_RAW_CSV
OUTPUT_PATH = TRAIN_SYNTHETIC_CSV

# ログ設定
setup_logger()
logger = logging.getLogger(__name__)


def main():
    # コア処理の呼び出し
    logger.info("学習用疑似データを生成します")
    synthetic_data = run_sdv_generation(INPUT_PATH, METADATA_JSON)

    # 保存処理
    synthetic_data.to_csv(OUTPUT_PATH, index=False)
    logger.info(f"学習用疑似データ生成が完了しました: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
