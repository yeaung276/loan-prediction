from typing import Any
import pandas as pd

# configs
TRAINING_DATA_PATH = "data/train_.csv"
TESTING_DATA_PATH = "data/test_.csv"
EMPTY_DATA_FILL_MODE = {"text": "mode", "number": "mean"}

DROP_COLUMNS = ["Loan_ID"]


def drop_columns(columns):
    csv_train = pd.read_csv(TRAINING_DATA_PATH)



drop_columns(DROP_COLUMNS)
