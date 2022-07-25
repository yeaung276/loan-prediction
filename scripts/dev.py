import os
import subprocess


def dev() -> None:
    """start dev server"""
    os.chdir("LoanPrediction")
    subprocess.run(["python", "main.py", "--dev"])


if __name__ == "__main__":
    dev()
