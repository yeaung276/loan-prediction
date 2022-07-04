import pandas as pd
from typing import Protocol
from pydantic import BaseModel


class PredictionModel(Protocol):
    def predict(self, X: pd.DataFrame) -> int:
        ...

    def predict_prob(self, X: pd.DataFrame) -> float:
        ...


class PredictionResult(BaseModel):
    result: int
    prob: float


class X(BaseModel):
    ...
