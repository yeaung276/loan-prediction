import os
import unittest
import pickle
import pandas as pd
import numpy as np
from modal.sklearn_modals.LR_modal import DataTransformer


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
                {
                    "Gender": ["Male"],
                    "Married": ["No"],
                    "Dependents": [0],
                    "Education": ["Graduate"],
                    "Self_Employed": ["No"],
                    "ApplicantIncome": [5849],
                    "CoapplicantIncome": [0],
                    "LoanAmount": [146.4112],
                    "Loan_Amount_Term": [360],
                    "Credit_History": [1],
                    "Property_Area": ["Urban"],
                }
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
