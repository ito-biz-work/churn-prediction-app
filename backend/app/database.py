from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import DATA_DIR

# データベースファイルのパス
DB_PATH = DATA_DIR / "churn.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# DBとの接続設定
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# DBとのやり取りを行うセッションクラス
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルの親クラス
Base = declarative_base()
