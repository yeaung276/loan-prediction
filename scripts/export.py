import os
import sys
import shutil

EXPORT_PATH = "LoanPrediction/core/model"
BASE_MODEL_PATH = "ModelTraining/output/"


def export(args: list[str] = sys.argv) -> None:
    model_name = args[1]
    src_dir = os.path.join(BASE_MODEL_PATH, model_name)
    dst_dir = os.path.join(EXPORT_PATH)
    try:
        shutil.copy(
            os.path.join(src_dir, f"{model_name}.pskl"),
            os.path.join(dst_dir, "model.pskl"),
        )
        shutil.copy(
            os.path.join(src_dir, f"{model_name}.log"),
            os.path.join(dst_dir, "description.txt"),
        )
    except FileNotFoundError as err:
        raise Exception("Model with given name does not exist!") from err


if __name__ == "__main__":
    export()
