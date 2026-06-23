from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from config.settings import DATA_DIR, DATABASE_NAME

# データベースファイルのパス
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATA_DIR}/{DATABASE_NAME}"

# DBとの接続設定
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# DBとのやり取りを行うセッションクラス
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルの親クラス
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
