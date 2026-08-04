import pytest

from config.settings import API_VERSION


def test_list_customers_success(client):
    """【200】顧客一覧の正常取得およびレスポンス構造の検証"""
    response = client.get(f"/api/{API_VERSION}/customers?skip=0&limit=5")

    # 検証
    assert response.status_code == 200
    data = response.json()
    assert "totalCount" in data
    assert "items" in data


def test_list_customers_invalid_skip(client):
    """【422】skipに不正な型（文字列）を指定した場合のエラー検証"""
    response = client.get(f"/api/{API_VERSION}/customers?skip=invalid")
    assert response.status_code == 422


@pytest.mark.parametrize(
    "params, description",
    [
        # skip の異常系
        ({"skip": "invalid"}, "【422】skipに不正な型（文字列）"),
        ({"skip": -1}, "【422】skipに範囲外の値（負の数）"),
        # limit の異常系
        ({"limit": "invalid"}, "【422】limitに不正な型（文字列）"),
        ({"limit": -1}, "【422】limitに範囲外の値（負の数）"),
    ],
)
def test_list_customers_invalid_query_params(client, params, description):
    """【422】顧客一覧APIのクエリパラメータに対するエラー検証"""
    response = client.get(f"/api/{API_VERSION}/customers", params=params)

    assert response.status_code == 422, f"エラー発生: {description}"
