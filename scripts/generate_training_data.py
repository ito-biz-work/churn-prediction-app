from config.settings import METADATA_JSON, RAW_DATA_DIR, SYNTHETIC_DATA_DIR
from scripts.data_utils.generator_core import run_sdv_generation

# パス設定
INPUT_PATH = RAW_DATA_DIR / "train.csv"
OUTPUT_PATH = SYNTHETIC_DATA_DIR / "train.csv"


def main():
    # コア処理の呼び出し
    print("疑似データを生成中...")
    synthetic_data = run_sdv_generation(INPUT_PATH, METADATA_JSON)

    # 保存処理
    synthetic_data.to_csv(OUTPUT_PATH, index=False)
    print(f"学習用データ生成完了: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
