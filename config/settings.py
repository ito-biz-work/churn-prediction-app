from pathlib import Path

# プロジェクトルートを特定
BASE_DIR = Path(__file__).resolve().parent.parent

# ディレクトリのパス
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
SYNTHETIC_DATA_DIR = DATA_DIR / "synthetic"

ML_MODEL_DIR = BASE_DIR / "backend" / "app" / "ml_models"

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
