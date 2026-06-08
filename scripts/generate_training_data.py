from config.settings import METADATA_JSON, TRAIN_RAW_CSV, TRAIN_SYNTHETIC_CSV
from scripts.data_utils.generator_core import run_sdv_generation

# パス設定
INPUT_PATH = TRAIN_RAW_CSV
OUTPUT_PATH = TRAIN_SYNTHETIC_CSV


def main():
    # コア処理の呼び出し
    print("疑似データを生成中...")
    synthetic_data = run_sdv_generation(INPUT_PATH, METADATA_JSON)

    # 保存処理
    synthetic_data.to_csv(OUTPUT_PATH, index=False)
    print(f"学習用データ生成完了: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
