from config.settings import METADATA_JSON, SYNTHETIC_DATA_DIR, TRAIN_CSV
from scripts.data_utils.generator_core import run_sdv_generation

# パス設定
OUTPUT_CSV = SYNTHETIC_DATA_DIR / "train.csv"


def main():
    # コア処理の呼び出し
    print("疑似データを生成中...")
    synthetic_data = run_sdv_generation(TRAIN_CSV, METADATA_JSON)

    # 保存処理
    synthetic_data.to_csv(OUTPUT_CSV, index=False)
    print(f"学習用データ生成完了: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
