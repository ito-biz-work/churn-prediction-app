from pathlib import Path

import category_encoders as ce
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

# パス設定
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "synthetic" / "train.csv"
MODEL_PATH = BASE_DIR / "backend" / "app" / "models" / "model.pkl"


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

    # 学習
    print("Training model...")
    pipe.fit(X, y)

    # 保存
    joblib.dump(pipe, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    train_and_save_model()
