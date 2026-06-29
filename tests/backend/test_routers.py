def test_list_customers(client):
    response = client.get("/api/v1/customers?skip=0&limit=5")

    # ステータスコード
    assert response.status_code == 200

    data = response.json()
    # キー
    assert "totalCount" in data
    assert "items" in data
