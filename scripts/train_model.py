from pathlib import Path

import category_encoders as ce
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

import mlflow
from config.settings import (
    ARTIFACT_DIR,
    EXPERIMENT_NAME,
    MLFLOW_DB,
    MODEL_JOBLIB,
    TRAIN_SYNTHETIC_CSV,
)

# パス設定
DATA_PATH = TRAIN_SYNTHETIC_CSV
MODEL_PATH = MODEL_JOBLIB
DB_PATH = MLFLOW_DB

# MLflow設定
mlflow.set_tracking_uri(f"sqlite:////{DB_PATH}")  # 保存場所

# エクスペリメントの存在チェックと作成
experiment = mlflow.get_experiment_by_name(EXPERIMENT_NAME)
if experiment is None:
    mlflow.create_experiment(
        EXPERIMENT_NAME, artifact_location=f"file://{ARTIFACT_DIR}"
    )

mlflow.set_experiment(EXPERIMENT_NAME)  # 実験名
mlflow.sklearn.autolog()  # 自動ロギングの有効化


def get_preprocessor():
    """前処理パイプラインの定義"""
    return ColumnTransformer(
        transformers=[
            ("state_count", ce.CountEncoder(), ["state"]),
            (
                "ohe",
                OneHotEncoder(sparse_output=False, handle_unknown="ignore"),
                ["area_code", "international_plan", "voice_mail_plan"],
            ),
        ],
        remainder="passthrough",
        verbose_feature_names_out=False,
    )


def train_and_save_model():
    """モデルを学習し、ファイルとして保存"""
    # データの読み込み
    df = pd.read_csv(DATA_PATH)
    X = df.drop(columns=["churn"])
    y = df["churn"].map({"no": 0, "yes": 1})

    # 整数型の列をfloat64に一括変換（MLflowの型エラー警告対策）
    int_cols = X.select_dtypes(include=["int64", "int32"]).columns
    X[int_cols] = X[int_cols].astype("float64")

    # パイプライン構築
    clf = RandomForestClassifier(
        n_estimators=100, random_state=42, class_weight="balanced"
    )
    pipe = Pipeline(
        [
            ("preprocessor", get_preprocessor()),
            ("classifier", clf),
        ]
    )

    # MLflowの記録を開始
    with mlflow.start_run(run_name="Production_Training"):
        # 学習
        print("学習中...")
        pipe.fit(X, y)

        # 親ディレクトリが存在しなければ作成する
        model_path = Path(MODEL_PATH)
        model_path.parent.mkdir(parents=True, exist_ok=True)

        # 保存
        joblib.dump(pipe, model_path)
        print(f"モデルを保存しました: {model_path}")


if __name__ == "__main__":
    train_and_save_model()
