import pandas as pd

from config.settings import API_VERSION, TEST_SYNTHETIC_CSV


def test_predict_endpoint_success(client):
    """WEBアプリ用疑似データCSVから1件抽出して、退会予測APIの挙動をテスト"""

    # CSVからデータを1行だけ読み込む
    df = pd.read_csv(TEST_SYNTHETIC_CSV, nrows=1)

    # PandasのデータをPydanticが受け取れる辞書（dict）形式に変換
    test_input = df.to_dict(orient="records")[0]

    # 補足：もしCSVに「customer_id」など、PredictionInputスキーマに
    # 含まれない不要な列がある場合は、ここでポップ（削除）してあげます
    # test_input.pop("id", None)

    response = client.post(f"/api/{API_VERSION}/predict", json=test_input)

    # 検証
    assert response.status_code == 200
    data = response.json()
    assert "probability" in data
    assert 0.0 <= data["probability"] <= 1.0
