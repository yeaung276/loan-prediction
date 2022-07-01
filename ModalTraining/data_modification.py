import pandas as pd

# configs
SAVE_INTRMEDIARY_FILES = False
RAW_DATA_PATH = "data"
INTERMEDIATE_FILE_PATH = "modal/intermediary_files"
MODIFIED_FILE_PATH = "modal/modified_data"
OUTPUT_STEP = 3

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
LABEL_COLUMN = "Loan_Status"
NORMALIZE_COLUMN = [
    "LoanAmount",
    "ApplicantIncome",
    "CoapplicantIncome",
    "Dependents",
    "Loan_Amount_Term",
]


def drop_columns(dataframe, columns):
    dataframe.drop(columns=columns, inplace=True)
    if SAVE_INTRMEDIARY_FILES:
        dataframe.to_csv(f"{INTERMEDIATE_FILE_PATH}/csv_drop_unnecessary_col.csv")


def fill_null_values_columns(dataframe, mean_columns, mode_columns):
    for column in mean_columns:
        dataframe[column].fillna(dataframe[column].mean(), inplace=True)
    for column in mode_columns:
        dataframe[column].fillna(dataframe[column].dropna().mode()[0], inplace=True)
    dataframe["Dependents"].replace("3+", 3, inplace=True)
    dataframe["Dependents"] = pd.to_numeric(dataframe["Dependents"])
    if SAVE_INTRMEDIARY_FILES:
        dataframe.to_csv(f"{INTERMEDIATE_FILE_PATH}/csv_filled_null.csv")


def encode_categorical(dataframe, categorical_columns):
    dataframe = pd.get_dummies(dataframe, columns=categorical_columns)
    if SAVE_INTRMEDIARY_FILES:
        dataframe.to_csv(f"{INTERMEDIATE_FILE_PATH}/csv_one_hot_encoded.csv")
    return dataframe


def encode_label(dataframe, column):
    dataframe[column].replace("Y", 1, inplace=True)
    dataframe[column].replace("N", 0, inplace=True)
    if SAVE_INTRMEDIARY_FILES:
        dataframe.to_csv(f"{INTERMEDIATE_FILE_PATH}/csv_label_encoded.csv")


def data_nomalization_min_max(dataframe, columns):
    for column in columns:
        d_min = dataframe[column].min()
        d_max = dataframe[column].max()
        dataframe[columns] = (dataframe[columns] - d_min) / (d_max - d_min)
    if SAVE_INTRMEDIARY_FILES:
        dataframe.to_csv(f"{INTERMEDIATE_FILE_PATH}/csv_normalized.csv")


def data_nomalization_div_by_mean(dataframe, columns):
    for column in columns:
        mean = dataframe[column].mean()
        dataframe[columns] = dataframe[columns] / mean
    if SAVE_INTRMEDIARY_FILES:
        dataframe.to_csv(f"{INTERMEDIATE_FILE_PATH}/csv_normalized.csv")


csv_train = pd.read_csv(f"{RAW_DATA_PATH}/train_.csv")
# step: 1
drop_columns(csv_train, DROP_COLUMNS)
if OUTPUT_STEP == 1:
    csv_train.to_csv(f"{MODIFIED_FILE_PATH}/train_.csv", index=False)
# step: 2
fill_null_values_columns(csv_train, MEANS_COLUMNS, MODE_COLUMNS)
if OUTPUT_STEP == 2:
    csv_train.to_csv(f"{MODIFIED_FILE_PATH}/train_.csv", index=False)
# step: 3
encode_label(csv_train, LABEL_COLUMN)
if OUTPUT_STEP == 3:
    csv_train.to_csv(f"{MODIFIED_FILE_PATH}/train_.csv", index=False)
# step: 4
csv_train = encode_categorical(csv_train, CATEGORICAL_COLUMNS)
if OUTPUT_STEP == 4:
    csv_train.to_csv(f"{MODIFIED_FILE_PATH}/train_.csv", index=False)
# step: 5
data_nomalization_div_by_mean(csv_train, NORMALIZE_COLUMN)
if OUTPUT_STEP == 5:
    csv_train.to_csv(f"{MODIFIED_FILE_PATH}/train_.csv", index=False)


print(csv_train.head())
print(csv_train.isnull().sum())
