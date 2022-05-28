from typing import Protocol
from xmlrpc.client import boolean
import pandas as pd
import pickle
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

MODAL_PATH = "../modal/logistic_regression_with_mean_normalization.pskl"

class Estimator:
    modal: ScikitModel

    def __init__(self) -> None:
        if self.modal is None:
            with open(MODAL_PATH, 'rb') as modal_file:
                self.modal = pickle.load(modal_file)

    def predict(self, X: pd.DataFrame) -> int:
        prediction = self.modal.predict(X)
        return prediction