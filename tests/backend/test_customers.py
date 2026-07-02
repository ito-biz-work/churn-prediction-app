def test_list_customers_endpoint_success(client):
    """顧客一覧の取得APIが正常に動作し、正しいレスポンス構造を返すかテスト"""
    response = client.get("/api/v1/customers?skip=0&limit=5")

    # 検証
    assert response.status_code == 200
    data = response.json()
    assert "totalCount" in data
    assert "items" in data
