import os
import sys
import shutil

EXPORT_PATH = "LoanPrediction/core/modal"
BASE_MODAL_PATH = "ModalTraining/output/"


def export(args: list[str] = sys.argv) -> None:
    modal_name = args[0]
    src_dir = os.path.join(BASE_MODAL_PATH, modal_name)
    dst_dir = os.path.join(EXPORT_PATH)
    shutil.copy(
        os.path.join(src_dir, f"{modal_name}.pskl"), os.path.join(dst_dir, "modal.pskl")
    )
    shutil.copy(
        os.path.join(src_dir, f"{modal_name}.log"),
        os.path.join(dst_dir, "description.txt"),
    )
