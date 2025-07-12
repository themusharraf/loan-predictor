from pydantic import BaseModel, Field
from typing import Literal


class PredictionRequest(BaseModel):
    loan_amount: float = Field(..., gt=0)
    income: float = Field(..., gt=0)
    term: Literal["Short Term", "Long Term"]
    emp_length: int = Field(..., ge=0, le=10)
    home_ownership: Literal["RENT", "MORTGAGE", "OWN", "OTHER"]
    purpose: str
    dti: float
    delinq_2yrs: int
    revol_util: float
    total_acc: int
    last_delinquent: int
