from app.models.model_loader import model
from app.utils.preprocessing import preprocess_input

def predict_loan(data: dict):
    model_features = model.feature_names_
    input_df = preprocess_input(data, model_features)

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    return {
        "prediction": int(prediction),
        "probability": probability
    }
