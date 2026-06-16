# --- 本番用
FROM python:3.12-slim

# セキュリティ対策: 非rootユーザーを作成
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# UVのインストールとパッケージ構築
RUN pip install uv

COPY pyproject.toml uv.lock ./
# 不要なキャッシュを削除し、システム全体にインストール
RUN uv pip install --system --no-cache -r pyproject.toml

COPY . .

# 権限設定: アプリケーションディレクトリの所有を変更
RUN chown -R appuser:appuser /app
USER appuser

# 実行コマンド
# --reloadを削除、本番向けのワーカー構成を追加
# WORKER_COUNTが設定されていなければ1を使う
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 8000 --workers ${WORKER_COUNT:-1}"]