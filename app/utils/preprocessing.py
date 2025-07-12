import numpy as np
import pandas as pd


def preprocess_input(data: dict, model_features: list[str]) -> pd.DataFrame:
    df = pd.DataFrame([{
        "Loan Amount": np.log1p(data["loan_amount"]),
        "Annual Income": np.log1p(data["income"]),
        "Term": data["term"],
        "Employment Length": data["emp_length"],
        "Home Ownership": data["home_ownership"],
        "Purpose": data["purpose"],
        "Debt-To-Income Ratio": data["dti"],
        "Delinquent 2yrs": data["delinq_2yrs"],
        "Revolving Utilization": data["revol_util"],
        "Total Accounts": data["total_acc"],
        "Months since last delinquent": data["last_delinquent"]
    }])

    df = pd.get_dummies(df)
    for col in model_features:
        if col not in df.columns:
            df[col] = 0
    return df[model_features]
