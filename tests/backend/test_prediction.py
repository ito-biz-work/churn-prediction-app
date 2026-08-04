import pandas as pd
import pytest

from config.settings import API_VERSION, TEST_SYNTHETIC_CSV


@pytest.fixture
def valid_input():
    """CSVから正常な入力データ（1件分の辞書）を読み込んで返す"""
    # CSVからデータを1行だけ読み込む
    df = pd.read_csv(TEST_SYNTHETIC_CSV, nrows=1)

    # PandasのデータをPydanticが受け取れる辞書（dict）形式に変換
    return df.to_dict(orient="records")[0]


def test_predict_success(client, valid_input):
    """WEBアプリ用疑似データCSVから1件抽出して、退会予測APIの挙動をテスト"""
    response = client.post(f"/api/{API_VERSION}/predict", json=valid_input)

    assert response.status_code == 200
    data = response.json()
    assert "probability" in data
    assert 0.0 <= data["probability"] <= 1.0


@pytest.mark.parametrize(
    "func, description",
    [
        # ボディが空
        (lambda d: {}, "【422】空のリクエストボディ"),
        # 必須フィールドが欠如
        (
            lambda d: {k: v for k, v in d.items() if k != "account_length"},
            "【422】必須フィールド(account_length)欠如",
        ),
        # 不正な型
        (
            lambda d: {**d, "account_length": "invalid_number"},
            "【422】不正なデータ型(account_lengthに文字列)",
        ),
        # 不正な値
        (
            lambda d: {**d, "account_length": -999},
            "【422】範囲外の値(account_lengthに負の数)",
        ),
    ],
)
def test_predict_invalid_body(client, valid_input, func, description):
    """【422】不正な入力データに対する予測APIのエラー検証"""
    # 正常なデータをもとに、テストケースごとの改変を適用
    invalid_input = func(valid_input.copy())

    response = client.post(f"/api/{API_VERSION}/predict", json=invalid_input)
    assert response.status_code == 422, f"エラー発生: {description}"
