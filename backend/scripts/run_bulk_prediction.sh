#!/bin/bash
set -e

# ==========================================
# ログ出力関数の定義 (Pythonのフォーマットに準拠)
# ==========================================

# INFOレベルのログ (標準出力)
log_info() {
    # ミリ秒付き日時形式(YYYY-MM-DD HH:MM:SS,mmm)
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S,000')
    echo "${timestamp} [INFO] $1"
}

# ERRORレベルのログ (標準エラー出力)
log_error() {
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S,000')
    echo "${timestamp} [ERROR] $1" >&2
}

# ==========================================
# 環境のセットアップ（コンテナ内外の両立）
# ==========================================

# 💡 1. コンテナの親プロセス（PID 1）が持つ環境変数を取り込む
# （コンテナ外で実行された場合はスルー）
if [ -f /proc/1/environ ]; then
    export $(tr '\0' '\n' < /proc/1/environ | grep -E 'DATABASE_URL|APP_DIR' 2>/dev/null || true)
fi

# 💡 2. コンテナ内のルート（/app）が存在すれば移動する
if [ -d /app ]; then
    cd /app
fi

# ==========================================
# メイン処理の実行
# ==========================================

log_info "バッチ処理を開始します"

# Pythonスクリプトを実行
if python backend/scripts/bulk_predict.py; then
    log_info "バッチ処理が完了しました"
else
    log_error "バッチ処理中にエラーが発生しました"
    exit 1
fi