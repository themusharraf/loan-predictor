from fastapi import FastAPI
from app.schemas.request import PredictionRequest
from app.services.predictor import predict_loan

app = FastAPI(title="Loan Default Prediction API")


@app.post("/predict")
async def predict(req: PredictionRequest):
    result = predict_loan(req.dict())
    return {
        "result": "Approved" if result["prediction"] == 1 else "Rejected",
        "probability": f"{result['probability']:.2%}"
    }
