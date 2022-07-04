import pickle
import pandas as pd
from LoanPrediction.core.Entity.est_data import X, PredictionModel, PredictionResult


MODEL_PATH = "../model/model.pskl"


class Estimator:
    model: PredictionModel

    def __init__(self) -> None:
        if self.model is None:
            with open(MODEL_PATH, "rb") as model_file:
                self.model = pickle.load(model_file)

    def predict(self, input: X) -> PredictionResult:
        X = pd.DataFrame(input.dict())
        prediction = self.model.predict(X)
        probability = self.model.predict_prob(X)
        return PredictionResult(result=prediction, prob=probability)
