import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routers import router as api_router
from config.settings import API_VERSION, setup_logger

# ログ設定
setup_logger()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Churn Prediction API",
    description="顧客の解約確率を予測する機械学習API",
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """全てのHTTPリクエストとレスポンス、および発生した例外をログに記録するミドルウェア"""
    logger.info(f"Request: {request.method} {request.url.path}")

    try:
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}")
        return response
    except Exception:
        logger.exception(f"Request failed: {request.method} {request.url.path}")
        raise


# 開発環境（ローカル）のViteのURLを許可
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# APIルーターの登録
app.include_router(api_router, prefix=f"/api/{API_VERSION}")
