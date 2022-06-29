import pickle
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

###############################################
# Simple Linear Regression With one hot encoding for categorical data and
# min-max standardization for numerical data
numerical_transformer = MinMaxScaler()
numerical_columns = [
    "LoanAmount",
    "ApplicantIncome",
    "CoapplicantIncome",
    "Dependents",
    "Loan_Amount_Term",
]

categorical_transformer = OneHotEncoder(handle_unknown="ignore", sparse=False)
categorical_columns = [
    "Gender",
    "Married",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Credit_History",
]

DataTransformer = ColumnTransformer(
    transformers=[
        ("numerical_transformation", numerical_transformer, numerical_columns),
        ("categorical_transformation", categorical_transformer, categorical_columns),
    ]
)

LinearModal = Pipeline(
    steps=[("transformer", DataTransformer), ("estimator", LinearRegression())]
)
