# --- 本番用
FROM python:3.12-slim

# セキュリティ対策: 非rootユーザーを作成
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# 環境変数
ENV APP_DIR=/app

# CRONのインストール
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# UVのインストールとパッケージ構築
RUN pip install uv

COPY pyproject.toml uv.lock ./

# 仮想環境を作らず、直接インストールする
# 不要なキャッシュを削除、開発用パッケージを除外
RUN uv export --frozen --no-dev -o requirements.txt
RUN uv pip install --system --no-cache -r requirements.txt

COPY . .

# 自作アプリ全体をPythonライブラリとして登録（本番用にコードを固定）
RUN uv pip install --system .

# カスタム設定ファイルをコンテナのCRONシステムに登録
COPY backend/scripts/crontab /etc/cron.d/bulk-predict-cron
RUN chmod 0644 /etc/cron.d/bulk-predict-cron
RUN crontab /etc/cron.d/bulk-predict-cron

# モデル生成を事前に行う
RUN python scripts/train_model.py

# CRONを一般ユーザーでも動かせるように特殊な権限（SUID）を付与
RUN chmod u+s /usr/sbin/cron

# 権限設定: アプリケーションディレクトリの所有を変更
RUN chown -R appuser:appuser /app
USER appuser

# 実行コマンド
# データシード投入、CRON起動、uvicorn起動
# --reloadは削除、本番向けのワーカー構成（設定無しは1）を追加
CMD ["sh", "-c", "python backend/scripts/seed_db.py && cron && exec uvicorn backend.main:app --host 0.0.0.0 --port 8000 --workers ${WORKER_COUNT:-1}"]