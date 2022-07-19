import pickle
import pandas as pd
from LoanPrediction.core.Entity.est_data import X, PredictionModel, PredictionResult


MODEL_PATH = "LoanPrediction/core/model/model.pskl"


class Estimator:
    """prediction services for giving the predicton result"""

    with open(MODEL_PATH, "rb") as model_file:
        model: PredictionModel = pickle.load(model_file)

    @classmethod
    def predict(cls, input: X) -> PredictionResult:
        """predict based on the result"""
        X = pd.DataFrame([input.dict()])
        prediction = cls.model.predict(X)[0]
        probability = cls.model.predict_proba(X)[0][1]
        return PredictionResult(result=prediction, prob=probability)
