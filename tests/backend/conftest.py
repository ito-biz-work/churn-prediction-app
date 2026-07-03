import os
from unittest.mock import patch

import numpy as np
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app.database import Base, get_db
from backend.app.models.customer_metrics import CustomerMetrics  # noqa: F401
from backend.main import app

# 環境変数からテスト用DBのURLを取得
TEST_DATABASE_URL = os.getenv("DATABASE_URL")

# エンジン作成
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    """テスト専用のデータベース環境を自動で準備・削除する"""
    # テスト開始時にテーブルを初期化
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    # テスト終了時にテーブルを削除
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    """テスト用のDBに繋いでくれるテスト専用の窓口"""

    def override_get_db():
        """テスト用のDBセッションを準備する関数"""
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()  # 終わったら差し替えを解除


@pytest.fixture(autouse=True)
def mock_ml_model():
    """本物のモデルファイルの代わりに、ダミーの予測結果を返す"""
    with patch("joblib.load") as mock_load:
        # get_pipeline() 経由で取得されるオブジェクトのモック
        mock_pipe = mock_load.return_value

        # pipe.classes_ が[0, 1] を返すように
        mock_pipe.classes_ = np.array([0, 1])

        # predict_proba が2次元配列を返すように
        mock_pipe.predict_proba.return_value = np.array([[0.85, 0.15]])

        yield
