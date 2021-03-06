import os
import unittest
import pickle
import pandas as pd
import numpy as np
from ModelTraining.sklearn_models.LR_model import DataTransformer


class TestDataTransformer(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        data = pd.read_csv("./tests/mocks/modified_test.csv")
        DataTransformer.fit(data)
        with open(f"./tests/modal.pskl", "wb") as modal_file:
            pickle.dump(DataTransformer, modal_file)

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove("./tests/modal.pskl")

    def setUp(self) -> None:
        with open(f"./tests/modal.pskl", "rb") as file:
            self.transformer = pickle.load(file)

    def test_data_transformation(self) -> None:
        result = self.transformer.transform(
            pd.DataFrame(
                [
                    {
                        "Married": "No",
                        "Gender": "Male",
                        "Education": "Graduate",
                        "Dependents": 0,
                        "ApplicantIncome": 5849,
                        "Self_Employed": "No",
                        "CoapplicantIncome": 0,
                        "Loan_Amount_Term": 360,
                        "LoanAmount": 146.4112,
                        "Credit_History": 1,
                        "Property_Area": "Urban",
                    }
                ]
            )
        )

        expected_array = [
            0.19885847,
            0.07048856,
            0,
            0,
            0.74358974,
            0,
            1,
            1,
            0,
            1,
            0,
            1,
            0,
            0,
            0,
            1,
            0,
            1,
        ]
        np.testing.assert_almost_equal(result[0], expected_array)
