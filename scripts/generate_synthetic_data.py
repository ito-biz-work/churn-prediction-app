from pathlib import Path

import pandas as pd
from sdv.metadata import Metadata
from sdv.single_table import CTGANSynthesizer

# パス設定
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "raw" / "train.csv"
OUTPUT_PATH = BASE_DIR / "data" / "synthetic" / "train.csv"
METADATA_PATH = BASE_DIR / "data" / "metadata.json"


def generate_synthetic_data(input_path, output_path, metadata_path, epochs=300):
    """
    指定されたメタデータに基づき、疑似データを生成してCSVとして保存する。

    Args:
        input_path (Path): 元データ（CSV）へのパス。
        output_path (Path): 生成したデータを保存する先のパス。
        metadata_path (Path): メタデータ（JSON）へのパス。

    Returns:
        None: 本関数は直接値を返さず、CSVファイルの出力のみを行う。
    """

    # 1. データ読み込み
    data = pd.read_csv(input_path)
    metadata = Metadata.load_from_json(metadata_path)

    # 2. 学習
    synthesizer = CTGANSynthesizer(metadata, epochs=epochs)
    synthesizer.fit(data)

    # 3. 生成
    synthetic_data = synthesizer.sample(num_rows=len(data))

    # 4. 型の整形
    dtype_map = data.dtypes.to_dict()
    for col, dtype in dtype_map.items():
        if col in synthetic_data.columns and dtype != "object":
            synthetic_data[col] = synthetic_data[col].astype(dtype)

    # 5. CSV保存
    synthetic_data.to_csv(output_path, index=False)
    print(f"データ生成完了: {output_path}")


if __name__ == "__main__":
    generate_synthetic_data(INPUT_PATH, OUTPUT_PATH, METADATA_PATH)
