import os
import sys
import shutil

EXPORT_PATH = "LoanPrediction/core/modal"
BASE_MODAL_PATH = "ModalTraining/output/"


def export(args: list[str] = sys.argv) -> None:
    modal_name = args[1]
    src_dir = os.path.join(BASE_MODAL_PATH, modal_name)
    dst_dir = os.path.join(EXPORT_PATH)
    try:
        shutil.copy(
            os.path.join(src_dir, f"{modal_name}.pskl"), os.path.join(dst_dir, "modal.pskl")
        )
        shutil.copy(
            os.path.join(src_dir, f"{modal_name}.log"),
            os.path.join(dst_dir, "description.txt"),
        )
    except FileNotFoundError as err:
        raise Exception('Modal with given name does not exist!') from err
