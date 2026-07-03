import logging
import os
import sys
from pathlib import Path

# プロジェクトルートを取得（環境変数があれば優先、なければ自動計算）
env_app_dir = os.environ.get("APP_DIR")
if env_app_dir:
    BASE_DIR = Path(env_app_dir)
else:
    BASE_DIR = Path(__file__).resolve().parent.parent

# ディレクトリのパス
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
SYNTHETIC_DATA_DIR = DATA_DIR / "synthetic"

BACKEND_DIR = BASE_DIR / "backend"
ML_MODEL_DIR = BACKEND_DIR / "app" / "ml_models"

MLFLOW_DIR = BASE_DIR / "mlflow"
ARTIFACT_DIR = MLFLOW_DIR / "artifacts"

# ファイルのパス
METADATA_JSON = DATA_DIR / "metadata.json"

TRAIN_RAW_CSV = RAW_DATA_DIR / "train.csv"
TRAIN_SYNTHETIC_CSV = SYNTHETIC_DATA_DIR / "train.csv"

TEST_RAW_CSV = RAW_DATA_DIR / "test.csv"
TEST_SYNTHETIC_CSV = SYNTHETIC_DATA_DIR / "test.csv"

MODEL_JOBLIB = ML_MODEL_DIR / "model.joblib"
MLFLOW_DB = MLFLOW_DIR / "mlflow.db"

# name
TABLE_NAME = "customer_metrics"
EXPERIMENT_NAME = "churn-prediction-experiment"


def setup_logger(level=logging.INFO):
    """システム全体のログ設定を一元管理する関数"""
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)  # 出力先を標準出力に明示
        ],
    )
