from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import DATABASE_NAME

# データベースファイルのパス
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

# DBとの接続設定
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# DBとのやり取りを行うセッションクラス
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルの親クラス
Base = declarative_base()
