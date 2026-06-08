from pathlib import Path

# プロジェクトルートを特定
BASE_DIR = Path(__file__).resolve().parent.parent

# ディレクトリのパス
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
SYNTHETIC_DATA_DIR = DATA_DIR / "synthetic"

# ファイルのパス
TRAIN_CSV = RAW_DATA_DIR / "train.csv"
METADATA_JSON = DATA_DIR / "metadata.json"
