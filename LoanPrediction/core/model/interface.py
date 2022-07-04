from typing import Literal
from pydantic import BaseModel, Field


class InputData(BaseModel):
    Gender: Literal["Male", "Female"]
    Married: Literal["Yes", "No"]
    Dependents: int = Field(..., ge=0, le=3)
    Education: Literal["Graduated", "Not Graduate"]
    Self_Employed: Literal["Yes", "No"]
    ApplicantIncome: int
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: bool
    ProPerty_Area: Literal["Urban", "Semiurban", "Rural"]
