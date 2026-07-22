import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from backend.app.prediction import load_pipeline
from backend.app.routers import router as api_router
from config.settings import API_VERSION, setup_logger

# ログ設定
setup_logger()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """FastAPIのライフスパンイベントで、サーバー起動時と停止時の処理を定義"""
    # サーバー起動時にモデルをロードして app.state に保存
    logger.info("サーバーを起動しています: 機械学習モデルをロード中")
    app.state.pipeline = load_pipeline()
    logger.info("機械学習モデルのロードが正常に完了しました")
    yield
    # サーバー停止時のクリーンアップ処理
    logger.info("サーバーを停止しています")
    app.state.pipeline = None


app = FastAPI(
    title="Churn Prediction API",
    description="顧客の解約確率を予測する機械学習API",
    lifespan=lifespan,
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
