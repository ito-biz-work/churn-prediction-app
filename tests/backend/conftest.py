import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.app.database import Base, get_db
from backend.app.models.customer_metrics import CustomerMetrics  # noqa: F401
from backend.main import app

# テスト用のDB（SQLiteのメモリモード）を作る
# メモリ上に作ることで、毎回まっさらな状態でテストする
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)  # テーブル作成
    yield
    Base.metadata.drop_all(bind=engine)  # 終わったら削除


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
