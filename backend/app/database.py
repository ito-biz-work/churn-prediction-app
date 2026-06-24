import os
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# データベースファイルのパス
SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]

# DBとの接続
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# セッション
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルの親クラス
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
