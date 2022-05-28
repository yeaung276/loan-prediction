import pickle
import pandas as pd
from LoanPrediction.core.Entity.est_data import ScikitModel


MODAL_PATH = "../modal/logistic_regression_with_mean_normalization.pskl"


class Estimator:
    modal: ScikitModel

    def __init__(self) -> None:
        if self.modal is None:
            with open(MODAL_PATH, "rb") as modal_file:
                self.modal = pickle.load(modal_file)

    def predict(self, X: pd.DataFrame) -> int:
        prediction = self.modal.predict(X)
        return int(prediction)
