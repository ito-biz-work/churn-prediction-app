from faker import Faker

from config.settings import METADATA_JSON, RAW_DATA_DIR, SYNTHETIC_DATA_DIR
from scripts.data_utils.generator_core import run_sdv_generation

# パス設定
INPUT_PATH = RAW_DATA_DIR / "test.csv"
OUTPUT_PATH = SYNTHETIC_DATA_DIR / "app.csv"

faker_jp = Faker("ja_JP")


def add_dummy_info(df):
    num_row = len(df)
    df["customer_code"] = [f"USR-{10000 + i}" for i in range(num_row)]
    df["customer_name"] = [faker_jp.name() for _ in range(num_row)]

    # codeと氏名を左端に配置
    cols = ["customer_code", "customer_name"] + [
        c for c in df.columns if c not in ["customer_code", "customer_name"]
    ]
    return df[cols]  # 新しいDFを返す


def main():
    # 共通の生成処理の呼び出し
    print("疑似データを生成中...")
    synthetic_data = run_sdv_generation(INPUT_PATH, METADATA_JSON)

    # 2. アプリ用データの加工
    print("ダミー情報を付与中...")
    app_data = add_dummy_info(synthetic_data)

    # 保存
    app_data.to_csv(OUTPUT_PATH, index=False)
    print(f"アプリ表示用データの生成が完了しました: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
