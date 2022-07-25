from typing import List
import argparse
import uvicorn
import config

parser = argparse.ArgumentParser(description="LoanPrediction web application")
parser.add_argument(
    "--host", type=str, nargs="?", default="0.0.0.0", help="host to run the application"
)
parser.add_argument(
    "--port",
    type=int,
    nargs="?",
    default=config.default_port,
    help="port the application listen",
)
parser.add_argument("--dev", action="store_true", help="is in dev mode or prod mode")
args = parser.parse_args()


def main() -> None:
    if args.dev:
        log_level = config.dev_log_level
    else:
        log_level = config.log_level
    uvicorn.run(
        "application.app:loanPredictionApp",
        host=args.host,
        port=args.port,
        log_level=log_level,
    )


if __name__ == "__main__":
    main()
