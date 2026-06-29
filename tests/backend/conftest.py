import os

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
    # テスト開始時にテーブルを初期化
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    # テスト終了時にテーブルを削除
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
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
