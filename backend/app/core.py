import joblib
import pandas as pd

from backend.app.schemas import PredictionInput
from config.settings import ML_MODEL_DIR

# パス設定
MODEL_PATH = ML_MODEL_DIR / "model.joblib"

# サーバー起動時に1回だけモデルをロード
model = joblib.load(MODEL_PATH)


def get_prediction(input_data: PredictionInput):
    """ "入力データを受け取り、モデルで推論して結果を返す"""
    # Pydanticモデルを辞書に変換し、PandasのDataFrameにする
    df = pd.DataFrame([input_data.model_dump()])

    # 推論
    # クラス予測
    prediction = int(model.predict(df)[0])
    # 確率を取得
    churn_index = list(model.classes_).index(1)  # 「1:yes」のラベルを探す
    probability = float(model.predict_proba(df)[0][churn_index])

    return {
        "churn_prediction": prediction,
        "churn_probability": probability,
    }
