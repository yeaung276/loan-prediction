import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_curve, roc_auc_score
from sklearn.linear_model import LogisticRegression

MODAL_NAME = "logistic_regression_with_mean_normalization"
MODAL_DESCRIPTION = "trained with div mean normalization on LoanAmount, ApplicantIncome, CoapplicantIncome, Dependent, Loan_Amount_Term"
TRAINING_DATA_PATH = "modal/datas/train_.csv"
Y_LABEL = "Loan_Status"
OUTPUT_PATH = "modal/intermediary_outputs"

data = pd.read_csv(TRAINING_DATA_PATH)

D_X = data.drop(Y_LABEL, axis=1)
D_Y = data[Y_LABEL]

X, X_test, Y, Y_test = train_test_split(D_X, D_Y, test_size=0.2)

# logistic regression
estimator = LogisticRegression()
estimator.fit(X, Y)
Y_p = estimator.predict(X_test)
accuracy = accuracy_score(Y_test, Y_p)
Y_pp = estimator.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(Y_test, Y_pp)
auc = roc_auc_score(Y_test, Y_pp)

# logging
info = {
    "name": MODAL_NAME,
    "description": MODAL_DESCRIPTION,
    "column_modification": "NONE",
    "columns": [col for col in X],
    "label": Y_LABEL,
    "accuracy": accuracy,
    "roc_accu": auc,
}
if not os.path.exists(f"{OUTPUT_PATH}/{MODAL_NAME}"):
    os.mkdir(f"{OUTPUT_PATH}/{MODAL_NAME}")

with open(f"{OUTPUT_PATH}/{MODAL_NAME}/{MODAL_NAME}.log", "w+") as log:
    log.write("Modal Summary\n")
    log.write("==============\n")
    for key, value in info.items():
        log.write(f"{key}: {value}")
        log.write("\n")
    log.write("End")

plt.plot(fpr, tpr, label="validation, auc=" + str(auc))
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend(loc=4)
plt.savefig(f"{OUTPUT_PATH}/{MODAL_NAME}/{MODAL_NAME}.png")

with open(f"{OUTPUT_PATH}/{MODAL_NAME}/{MODAL_NAME}.pskl", "wb") as modal_file:
    pickle.dump(estimator, modal_file)

data.to_csv(f"{OUTPUT_PATH}/{MODAL_NAME}/{MODAL_NAME}.csv")
