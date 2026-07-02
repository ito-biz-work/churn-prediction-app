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

import mlflow
from config.settings import ARTIFACT_DIR, EXPERIMENT_NAME, MLFLOW_DB

## 0. MLflowの設定

# %%
# MLflowの定数とURI設定
DB_PATH = MLFLOW_DB
mlflow.set_tracking_uri(f"sqlite:////{DB_PATH}")  # 保存場所

# %%
# エクスペリメントの存在チェックと作成
experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
if experiment is None:
    mlflow.create_experiment(
        EXPERIMENT_NAME, artifact_location=f"file://{ARTIFACT_DIR}"
    )

# %%
# MLflowの初期設定
mlflow.set_experiment(EXPERIMENT_NAME)  # 実験名
mlflow.sklearn.autolog()  # 自動ロギングの有効化


## 1. 探索的分析 EDA

# %%
# データの読み込み
df = pd.read_csv("../data/synthetic/train.csv")
df.head(3)

# %%
# 欠損値の確認
df.isnull().sum()

# %%
# 正解データの比率
df["churn"].value_counts(normalize=True)

# %%
# カテゴリ変数のユニーク数を確認
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

# 整数型の列をfloat64に一括変換（MLflowの型エラー警告対策）
int_cols = X.select_dtypes(include=["int64", "int32"]).columns
X[int_cols] = X[int_cols].astype("float64")

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
# CountEncoding + OneHotEncoding
count_encoder = ce.CountEncoder()
ohe_encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")

# 変換
preprocessor = ColumnTransformer(
    transformers=[
        ("state_count", count_encoder, ["state"]),
        ("ohe", ohe_encoder, ["area_code", "international_plan", "voice_mail_plan"]),
    ],
    remainder="passthrough",
    verbose_feature_names_out=False,  # prefix無し
)

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
    # モデルごとに新しい記録を開始する
    with mlflow.start_run(run_name=f"CV_{name}"):
        # タグ登録
        mlflow.set_tag("stage", "cv")
        mlflow.set_tag("algorithm", name)

        pipe = Pipeline([("preprocessor", preprocessor), ("classifier", model)])

        # 正解率/AUCを指標として、交差検証を実施
        cv_results = cross_validate(
            pipe, X_train, y_train, cv=cv, scoring=["accuracy", "roc_auc"]
        )

        # 集計
        results_df = pd.DataFrame(cv_results)
        mean_acc = results_df["test_accuracy"].mean()
        mean_auc = results_df["test_roc_auc"].mean()

        summary = {
            "Model-Name": name,
            "Accuracy-Mean": mean_acc,
            "AUC-Mean": mean_auc,
            "Fit-Time-Sum": results_df["fit_time"].sum(),
        }
        result_all.append(summary)

        # 交差検証の平均スコアを記録
        mlflow.log_metric("cv_accuracy_mean", mean_acc)
        mlflow.log_metric("cv_auc_mean", mean_auc)

# 結果を一括表示
result_all_df = pd.DataFrame(result_all)
print(f"--- {n_splits}分割交差検証 ---")
print(result_all_df)

## 3. テストデータの前処理～評価まで

# %%
# テスト
# 一番スコアが良かったモデルを採用

# 自動：「AUC-Mean」が最大（一番スコアが良い）の行を探す
best_row = result_all_df.loc[result_all_df["AUC-Mean"].idxmax()]
best_model_name = best_row["Model-Name"]
# 手動
# best_model_name = "RandomForest"

best_model = models[best_model_name]

# 最終モデルの記録用に新しいRunを開始
with mlflow.start_run(run_name=f"Final_{best_model_name}"):
    # タグ登録
    mlflow.set_tag("stage", "final")
    mlflow.set_tag("algorithm", best_model_name)

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

    # テストデータの評価指標を記録
    mlflow.log_metric("test_accuracy", final_acc)
    mlflow.log_metric("test_auc", final_auc)

    print(f"--- テストデータ検証 {best_model_name} ---")
    print(f"Accuracy: {final_acc:.2f}")
    print(f"AUC : {final_auc:.2f}")

# %%
# 特徴量重要度

# パイプライン内の各ステップにアクセス
model_step = final_pipe.named_steps["classifier"]
preprocessor_step = final_pipe.named_steps["preprocessor"]

# 特徴量名の取得
# OHEやカウントエンコーディング後の名前を取る
feature_names = preprocessor_step.get_feature_names_out()

# 重要度の取得
importances = model_step.feature_importances_

# DataFrame化
feature_importances_df = pd.DataFrame(
    {"feature": feature_names, "importance": importances}
).sort_values(by="importance", ascending=False)

print("--- 特徴量の重要度 ---")
# print(feature_importances_df.head(10))  # 上位10個を表示
print(feature_importances_df.head(7))  # 上位7個を表示
