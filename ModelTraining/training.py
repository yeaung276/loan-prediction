import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_curve, roc_auc_score
from ModelTraining.sklearn_models.LR_model import LinearModel

MODAL_NAME = "logistic_regression_with_pipeline"
MODAL_DESCRIPTION = "first test with pipe line"
TRAINING_DATA_PATH = "ModelTraining/modified_data/train_.csv"
Y_LABEL = "Loan_Status"
OUTPUT_PATH = "ModelTraining/output"

data = pd.read_csv(TRAINING_DATA_PATH)

# data, label splitting
D_X = data.drop(Y_LABEL, axis=1)
D_Y = data[Y_LABEL]

# train, test splitting
X, X_test, Y, Y_test = train_test_split(D_X, D_Y, test_size=0.2)

# modal training
LinearModel.fit(X, Y)

# modal evaluation
Y_p = LinearModel.predict(X_test)
accuracy = accuracy_score(Y_test, Y_p)
Y_pp = LinearModel.predict_proba(X_test)[:, 1]
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

# saving the modal
with open(f"{OUTPUT_PATH}/{MODAL_NAME}/{MODAL_NAME}.pskl", "wb") as modal_file:
    pickle.dump(LinearModel, modal_file)

# saving the modal info
data.to_csv(f"{OUTPUT_PATH}/{MODAL_NAME}/{MODAL_NAME}.csv", index=False)
