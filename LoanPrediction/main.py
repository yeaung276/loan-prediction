import sys
import os
from typing import List
import uvicorn
import LoanPrediction.config as config


def main(args: List[str] = sys.argv) -> None:
    path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path)
    uvicorn.run(
        "application.app:loanPredictionApp",
        host=args[1],
        port=int(args[2]),
        log_level=config.log_level,
    )


def dev() -> None:
    print(os.getcwd())
    path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path)
    print(os.getcwd())
    uvicorn.run(
        "application.app:loanPredictionApp",
        host="0.0.0.0",
        port=3030,
        log_level=config.dev_log_level,
        reload=True,
    )


if __name__ == "__main__":
    main()
