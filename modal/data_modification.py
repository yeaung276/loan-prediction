import pandas as pd
from pyparsing import col

# configs
TRAINING_DATA_PATH = "data/train_.csv"
TESTING_DATA_PATH = "data/test_.csv"
SAVE_FILE_PATH = "modal/intermediary_files"

DROP_COLUMNS = ["Loan_ID"]
MEANS_COLUMNS = ["LoanAmount", "ApplicantIncome", "CoapplicantIncome"]
MODE_COLUMNS = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Loan_Amount_Term",
    "Credit_History",
]
CATEGORICAL_COLUMNS = [
    "Gender",
    "Married",
    "Education",
    "Self_Employed",
    "Property_Area",
]


def drop_columns(dataframe, columns):
    dataframe.drop(columns=columns, inplace=True)
    dataframe.to_csv(f"{SAVE_FILE_PATH}/csv_drop_unnecessary_col.csv")


def fill_null_values_columns(dataframe, mean_columns, mode_columns):
    for column in mean_columns:
        dataframe[column].fillna(dataframe[column].mean(), inplace=True)
    for column in mode_columns:
        dataframe[column].fillna(dataframe[column].dropna().mode()[0], inplace=True)
    dataframe["Dependents"].replace("3+", 3, inplace=True)
    dataframe.to_csv(f"{SAVE_FILE_PATH}/csv_filled_null.csv")


def encode_categorical(dataframe, categorical_columns):
    dataframe = pd.get_dummies(dataframe, columns=categorical_columns)
    dataframe.to_csv(f"{SAVE_FILE_PATH}/csv_one_hot_encoded.csv")
    return dataframe


csv_train = pd.read_csv(TRAINING_DATA_PATH)
# step: 1
drop_columns(csv_train, DROP_COLUMNS)
# step: 2
fill_null_values_columns(csv_train, MEANS_COLUMNS, MODE_COLUMNS)
# step: 3
csv_train = encode_categorical(csv_train, CATEGORICAL_COLUMNS)

print(csv_train.isnull().sum())
