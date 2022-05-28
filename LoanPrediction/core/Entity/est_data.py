import pandas as pd
from typing import Protocol
from pydantic import BaseModel

class ScikitModel(Protocol):
    def predict(self, X: pd.DataFrame) -> int:
        ...

class X(BaseModel):
    Dependents: int
    ApplicantIncome: int
    CoapplicantIncome: int
    LoanAmount: int
    Loan_Amount_Term: int
    Credit_History: bool
    Gender_Female: bool
    Gender_Male: bool
    Married_Yes: bool
    Education_Graduate: bool
    Self_Employed_Yes: bool
    Property_Area_Rural: bool
    Property_Area_Semiurban: bool
    Property_Area_Urban: bool