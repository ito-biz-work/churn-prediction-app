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