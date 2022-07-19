import unittest
from LoanPrediction.core.Entity.est_data import X
from LoanPrediction.core.Service.estimation import Estimator


class TestEstimator(unittest.TestCase):
    def setUp(self) -> None:
        self.estimator = Estimator()

    def test_predict(self) -> None:
        test_data = X(
            Gender="Male",
            Married="Yes",
            Dependents=2,
            Education="Graduated",
            Self_Employed="Yes",
            ApplicantIncome=3000,
            CoapplicantIncome=2000,
            LoanAmount=5000,
            Loan_Amount_Term=230,
            Credit_History=True,
            Property_Area="Urban",
        )
        result = self.estimator.predict(test_data)
        print(result.result, "what")
        assert result.result == 1 or result.result == 0
        assert 0 < result.prob < 1
