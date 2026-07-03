# --- 本番用
FROM python:3.12-slim

# セキュリティ対策: 非rootユーザーを作成
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# UVのインストールとパッケージ構築
RUN pip install uv

COPY pyproject.toml uv.lock ./

# 仮想環境を作らず、直接インストールする
# 不要なキャッシュを削除、開発用パッケージを除外
RUN uv export --frozen --no-dev -o requirements.txt
RUN uv pip install --system --no-cache -r requirements.txt

COPY . .

# 自作アプリ全体をPythonライブラリとして登録（本番用にコードを固定）
RUN uv pip install --system -e .

# モデル生成を事前に行う
# PYTHONPATH を設定して、/app をルートモジュールとして認識させる
RUN PYTHONPATH=. python scripts/train_model.py

# 権限設定: アプリケーションディレクトリの所有を変更
RUN chown -R appuser:appuser /app
USER appuser

# 実行コマンド
# --reloadを削除、本番向けのワーカー構成（設定無しは1）を追加
# データシード投入を行う
CMD ["sh", "-c", "PYTHONPATH=. python backend/scripts/seed_db.py && uvicorn backend.main:app --host 0.0.0.0 --port 8000 --workers ${WORKER_COUNT:-1}"]