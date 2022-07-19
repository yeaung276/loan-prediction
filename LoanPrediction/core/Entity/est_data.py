import pandas as pd
from typing import List, Protocol
from pydantic import BaseModel
from LoanPrediction.core.model.interface import InputData


class PredictionModel(Protocol):
    def predict(self, X: pd.DataFrame) -> List[int]:
        ...

    def predict_proba(self, X: pd.DataFrame) -> List[List[float]]:
        ...


class PredictionResult(BaseModel):
    result: int
    prob: float


class X(InputData):
    ...
