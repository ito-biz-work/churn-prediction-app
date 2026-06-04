# %%
import category_encoders as ce
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

## 1. 探索的分析 EDA

# %%
# データの読み込み
df = pd.read_csv("../data/raw/train.csv")
df.head(3)

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

## 2. 訓練データの前処理～評価まで

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
# エンコーディング
# state列は51種類（データ分割前）と多いため、CountEncodingを実施。
# TargetEncodingによるデータリークを考慮し、まずは安全な方法を選択。
# 残りのカテゴリ変数の列は、OneHotEncodingで対応。
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

# %%
# まずはダミーモデルのみk分割交差検証を実施
# # パイプライン
# pipe = Pipeline(
#     [
#         ("preprocessor", preprocessor),
#         ("dummy_classifier", DummyClassifier(strategy="most_frequent")),
#     ]
# )

# # k分割交差検証
# cv = StratifiedKFold(n_splits=5, random_state=42, shuffle=True)

# # 正解率/AUCを指標として、交差検証を実施
# cv_results = cross_validate(
#     pipe, X_train, y_train, cv=cv, scoring=["accuracy", "roc_auc"]
# )

# # 結果表示
# results_df = pd.DataFrame(cv_results)
# print("--- 交差検証結果の詳細 ---")
# print(results_df)

# # 平均値をまとめて確認
# print("\n--- スコアの要約 ---")
# print(results_df.mean())

# print("\n--- 平均値の抜粋 ---")
# print(f"平均正解率: {results_df['test_accuracy'].mean():.2f}")
# print(f"平均AUC: {results_df['test_roc_auc'].mean():.2f}")

# %%
# 全モデルでk分割交差検証を実施
n_splits = 5
cv = StratifiedKFold(n_splits=n_splits, random_state=42, shuffle=True)

# モデルを辞書に格納
models = {
    "Dummy": DummyClassifier(strategy="most_frequent"),
    "DecisionTree": DecisionTreeClassifier(
        max_depth=3,
        random_state=42,
        class_weight="balanced",  # 不均衡データを考慮
    ),
    "RandomForest": RandomForestClassifier(
        n_estimators=100,
        max_depth=None,
        random_state=42,
        class_weight="balanced",
    ),
}

result_all = []
for name, model in models.items():
    pipe = Pipeline([("preprocessor", preprocessor), ("classifier", model)])

    # 正解率/AUCを指標として、交差検証を実施
    cv_results = cross_validate(
        pipe, X_train, y_train, cv=cv, scoring=["accuracy", "roc_auc"]
    )

    # 結果を見やすくするために集計
    results_df = pd.DataFrame(cv_results)
    summary = {
        "Model-Name": name,
        "Accuracy-Mean": results_df["test_accuracy"].mean(),
        "AUC-Mean": results_df["test_roc_auc"].mean(),
        "Fit-Time-Sum": results_df["fit_time"].sum(),
    }
    result_all.append(summary)

# 結果を一括表示
result_all_df = pd.DataFrame(result_all)
print(f"--- {n_splits}分割交差検証 ---")
print(result_all_df)

## 3. テストデータの前処理～評価まで

# %%
# テスト
# 一番スコアが良かったモデルを採用
best_model_name = "RandomForest"
best_model = models[best_model_name]

# 再度パイプラインを構築
final_pipe = Pipeline(
    [
        ("preprocessor", preprocessor),
        ("classifier", best_model),
    ]
)

# 訓練データ全体で学習
final_pipe.fit(X_train, y_train)

# テストデータで予測
y_pred_classes = final_pipe.predict(X_test)
y_pred_probs = final_pipe.predict_proba(X_test)[:, 1]

final_acc = accuracy_score(y_test, y_pred_classes)
final_auc = roc_auc_score(y_test, y_pred_probs)

print(f"--- テストデータ検証 {best_model_name} ---")
print(f"Accuracy: {final_acc:.2f}")
print(f"AUC : {final_auc:.2f}")

# %%
