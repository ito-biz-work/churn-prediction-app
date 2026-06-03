# %%
import category_encoders as ce
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

## 1. 探索的分析 EDA

# %%
# データの読み込み
df = pd.read_csv("../data/raw/train.csv")
df.head(3)

# %%
# 統計量
# df.describe()
# df.describe(include="all")

# %%
# 欠損値の確認
df.isnull().sum()

# %%
# 正解データの比率
df["churn"].value_counts(normalize=True)

# %%
# カテゴリ変数のユニーク数を確認
# object型（カテゴリ変数）の列だけを抽出
categorical_cols = df.select_dtypes(include=["string", "object"]).columns

print("categorical_cols count: ", len(categorical_cols))

# 降順ソート
df[categorical_cols].nunique().sort_values(ascending=False)

## 2. 訓練データの前処理

# %%
# データ分割
X = df.drop(columns=["churn"])
y = df["churn"]

# 目的変数を数値化する
y = y.map({"no": 0, "yes": 1})

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,  # 不均衡データを考慮
)

# shape
print("X_train", X_train.shape)
print("X_test", X_test.shape)
print("y_train", y_train.shape)
print("y_test", y_test.shape)

# %%
# 頻度エンコーディング
# state列は51種類（データ分割前）と多いため、OneHotEncodingを避けてCountEncodingを実施。
# TargetEncodingによるデータリークを考慮し、まずは安全な方法を選択。

# count_encoder = ce.CountEncoder(cols=["state"])
# X_train["state_encoded"] = count_encoder.fit_transform(X_train["state"])
# X_train = X_train.drop(columns=["state"])
# X_train.head(3)

# %%
# ワンホットエンコーディング
# ユニーク数が少ないカテゴリ変数の列は、OneHotEncodingで対応

# ohe_encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
# preprocessor = ColumnTransformer(
#     transformers=[
#         ("ohe", ohe_encoder, ["area_code", "international_plan", "voice_mail_plan"]),
#     ],
#     remainder="passthrough",
# )
# X_train_processed = preprocessor.fit_transform(X_train)

# %%
# 2つのエンコーディングをまとめて実行
count_encoder = ce.CountEncoder()
ohe_encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")

# 変換
preprocessor = ColumnTransformer(
    transformers=[
        ("state_count", count_encoder, ["state"]),
        ("ohe", ohe_encoder, ["area_code", "international_plan", "voice_mail_plan"]),
    ],
    remainder="passthrough",  # 残りの列（数値列など）はそのまま保持
    verbose_feature_names_out=False,  # prefix無し
)

# numpy.ndarrayで返る
X_train_processed = preprocessor.fit_transform(X_train)

# %%
# shapeの確認（再）
print("X_train", X_train.shape)
print("X_train_processed", X_train_processed.shape)

# %%
# 欠損値の確認（再）
nan_count_train = np.isnan(X_train_processed).sum()
print(f"欠損値の個数: {nan_count_train}")

## 3. テストデータの前処理

# %%
X_test_processed = preprocessor.transform(X_test)

# %%
# shapeの確認（再）
print("X_test", X_test.shape)
print("X_test_processed", X_test_processed.shape)

# %%
# 欠損値の確認（再）
nan_count_test = np.isnan(X_test_processed).sum()
print(f"欠損値の個数: {nan_count_test}")

## 4. モデルによる学習と評価

# %%
# ダミーモデル（最頻値）
dummy_clf = DummyClassifier(strategy="most_frequent")
dummy_clf.fit(X_train_processed, y_train)

dummy_pred = dummy_clf.predict(X_test_processed)
# 1（退会する）確率だけを抜き出す
dummy_probs = dummy_clf.predict_proba(X_test_processed)[:, 1]

dummy_acc = accuracy_score(y_test, dummy_pred)
dummy_auc = roc_auc_score(y_test, dummy_probs)

print(f"ダミーモデル 正解率: {dummy_acc:.2f}")
print(f"ダミーモデル AUC : {dummy_auc:.2f}")

# %%
# 決定木（分類木）
dt_clf = DecisionTreeClassifier(
    max_depth=3,
    random_state=42,
    class_weight="balanced",  # 不均衡データを考慮
)
dt_clf.fit(X_train_processed, y_train)

dt_pred = dt_clf.predict(X_test_processed)
dt_probs = dt_clf.predict_proba(X_test_processed)[:, 1]

dt_acc = accuracy_score(y_test, dt_pred)
dt_auc = roc_auc_score(y_test, dt_probs)

print(f"決定木 正解率: {dt_acc:.2f}")
print(f"決定木 AUC : {dt_auc:.2f}")

# %%
# 決定木の特徴量重要度
# pd.Series(dt_clf.feature_importances_, index=feature_names).sort_values(ascending=False)

# %%
# ランダムフォレスト
rf_clf = RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    random_state=42,
    class_weight="balanced",  # 不均衡データを考慮
)
rf_clf.fit(X_train_processed, y_train)

rf_pred = rf_clf.predict(X_test_processed)
rf_probs = rf_clf.predict_proba(X_test_processed)[:, 1]

rf_acc = accuracy_score(y_test, rf_pred)
rf_auc = roc_auc_score(y_test, rf_probs)

print(f"ランダムフォレスト 正解率: {rf_acc:.2f}")
print(f"ランダムフォレスト AUC : {rf_auc:.2f}")

# %%
# ランダムフォレストの特徴量重要度
# pd.Series(rf_clf.feature_importances_, index=feature_names).sort_values(ascending=False)

# %%
