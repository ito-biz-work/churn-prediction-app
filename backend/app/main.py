from fastapi import FastAPI

from .app import router as api_router

app = FastAPI(
    title="Churn Prediction API",
    description="顧客の解約確率を予測する機械学習API",
)
app.include_router(api_router, prefix="/api/v1")
