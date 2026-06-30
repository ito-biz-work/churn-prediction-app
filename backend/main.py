import logging
import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routers import router as api_router

logging.basicConfig(level=logging.INFO)
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
    except Exception as e:
        logger.error(f"Error:{e}", exc_info=True)
        raise


# Reactアプリが動くURLを許可
allowed_origins_raw = os.environ.get("CORS_ALLOWED_ORIGINS")
origins = allowed_origins_raw.split(",")  # 文字列から配列に分解

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# APIルーターの登録
app.include_router(api_router, prefix="/api/v1")
