from fastapi import FastAPI
from loanprediction.application.services.routes import mainRouter

loanPredictionApp = FastAPI()

loanPredictionApp.include_router(mainRouter)


@loanPredictionApp.get("/")
async def welcome() -> str:
    return "Welcome from Loan prediction app using fastapi"


@loanPredictionApp.get("/version")
async def version() -> str:
    return "version"
