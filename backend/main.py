import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routers import router as api_router

app = FastAPI(
    title="Churn Prediction API",
    description="顧客の解約確率を予測する機械学習API",
)

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
