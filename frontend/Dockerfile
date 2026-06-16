# --- 本番用

# --- ステージ1: ビルド
FROM node:22-slim AS builder
WORKDIR /app

# 依存関係のインストール
RUN corepack enable
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

COPY . .
RUN pnpm run build

# --- ステージ2: 配信
FROM nginx:alpine

# Nginxの設定ファイルをコピー（※作成が必要）
# 画面遷移が発生する場合は、必要
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# ビルドした成果物をコピー
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]