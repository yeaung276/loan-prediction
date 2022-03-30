import uvicorn
import loanprediction.config as config


def main() -> None:
    uvicorn.run(
        "loanprediction.application.app:loanPredictionApp",
        host=config.host,
        port=config.port,
        log_level=config.log_level,
    )


def dev() -> None:
    uvicorn.run(
        "loanprediction.application.app:loanPredictionApp",
        host=config.host,
        port=config.port,
        log_level=config.dev_log_level,
        reload=True,
    )


if __name__ == "__main__":
    main()
