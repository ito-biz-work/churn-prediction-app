from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app import router as api_router

app = FastAPI(
    title="Churn Prediction API",
    description="顧客の解約確率を予測する機械学習API",
)

# Reactアプリが動くURLを許可
origins = ["http://localhost:5173"]  # Viteのデフォルトポート

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#
app.include_router(api_router, prefix="/api/v1")
