# %%
import numpy as np
import pandas as pd
from sdv.evaluation.single_table import evaluate_quality
from sdv.metadata import Metadata
from sdv.single_table import CTGANSynthesizer

# %%
# 元データの読み込み
data = pd.read_csv("../data/raw/train.csv")
data.head(2)

# # %%
# metadata.jsonを利用して、疑似データを生成
metadata = Metadata.load_from_json("../data/metadata.json")

# # Metadataクラスの作成とデータの読み込み
# # データ型やカラムの構造を定義
# metadata = Metadata.detect_from_dataframe(data)

# # メタデータを保存
# # metadata.save_to_json("../data/metadata.json")

# CTGANモデルの初期化と学習
epochs = 300  # 300 がデフォルト
synthesizer = CTGANSynthesizer(metadata, epochs=epochs)
synthesizer.fit(data)

# 疑似データの生成（元データと同じ行数分）
synthetic_data = synthesizer.sample(num_rows=len(data))

# 疑似データ確認
synthetic_data.head(3)


# %%
# 類似度の評価
def print_quality(data, synthetic_data, metadata, epochs):
    report = evaluate_quality(
        real_data=data, synthetic_data=synthetic_data, metadata=metadata
    )
    print(f"epochs: {epochs}")
    print(f"品質スコア: {report.get_score():.2f}")


# 評価
# epochs=100 : 0.84
# epochs=300 : 0.89
# epochs=400 : 0.89
print_quality(data, synthetic_data, metadata, epochs)

# %%
# どのカラムのスコアが低いのかを確認
# detail_df = report.get_details(property_name="Column Shapes").sort_values(
#     by="Score", ascending=False
# )
# print(detail_df)

# %%
# ノイズ付加
# 数値型（int, float）の列だけを抽出
numeric_cols = synthetic_data.select_dtypes(include=[np.number]).columns

# 全ての数値カラムに対して、元の値の±5%の範囲でランダムなノイズを加える
noise_factor = 0.05
synthetic_data[numeric_cols] = synthetic_data[numeric_cols].apply(
    lambda x: x * (1 + np.random.normal(0, noise_factor, len(x)))
)

# %%
# ノイズ付加後の評価
# epochs=300 : 0.87
print_quality(data, synthetic_data, metadata, epochs)

# %%
# 最小値チェック
print(synthetic_data.min())

# %%
# 元データとの重複チェック

# 型の定義を抽出
dtype_map = data.dtypes.to_dict()

# インデックスをリセットして純粋なデータだけにする
check_real = data.reset_index(drop=True)
check_synth = synthetic_data.reset_index(drop=True)

# 疑似データに対して、参照した型を適用
for col, dtype in dtype_map.items():
    if col in check_synth.columns:
        if dtype != "object":
            check_synth[col] = check_synth[col].astype(dtype)

# 重複チェック
duplicates = pd.merge(check_real, check_synth, how="inner", on=list(data.columns))
print(f"元データと完全に一致する行数: {len(duplicates)}")

if not duplicates.empty:
    print(duplicates.head())

# %%
