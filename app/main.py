from fastapi import FastAPI
from app.schemas.request import PredictionRequest
from app.services.predictor import predict_loan
from app.core.logger import setup_logger
from app.core.middlewares import LoggingMiddleware
from app.metrics.prometheus import prometheus_middleware, router as metrics_router

setup_logger()

app = FastAPI(title="Loan Default Prediction API")
app.add_middleware(LoggingMiddleware)
app.middleware("http")(prometheus_middleware)
app.include_router(metrics_router)


@app.post("/predict")
async def predict(req: PredictionRequest):
    result = predict_loan(req.dict())
    return {
        "result": "Approved" if result["prediction"] == 1 else "Rejected",
        "probability": f"{result['probability']:.2%}"
    }
