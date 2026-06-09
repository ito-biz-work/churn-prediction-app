import pandas as pd
from sdv.metadata import Metadata
from sdv.single_table import CTGANSynthesizer


def run_sdv_generation(input_path, metadata_path, epochs=300, is_training=True):
    """共通の学習・生成処理を行うコア関数"""
    # データとメタデータの読み込み
    data = pd.read_csv(input_path)
    metadata = Metadata.load_from_json(metadata_path)

    # 調整
    if not is_training:
        data = data.drop(columns=["id"])  # 学習対象から外す
        metadata.remove_column(column_name="churn")  # 目的変数項目は削除

    # 学習
    synthesizer = CTGANSynthesizer(metadata, epochs=epochs)
    synthesizer.fit(data)

    # 生成
    synthetic_data = synthesizer.sample(num_rows=len(data))

    # 型の整形
    dtype_map = data.dtypes.to_dict()
    for col, dtype in dtype_map.items():
        if col in synthetic_data.columns and dtype != "object":
            synthetic_data[col] = synthetic_data[col].astype(dtype)

    return synthetic_data
