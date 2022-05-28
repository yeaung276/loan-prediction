from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loanprediction.application.routes.routes import mainRouter

loanPredictionApp = FastAPI()

loanPredictionApp.include_router(mainRouter)

loanPredictionApp.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@loanPredictionApp.get("/")
async def welcome() -> str:
    return "Welcome from Loan prediction app using fastapi"


@loanPredictionApp.get("/version")
async def version() -> str:
    return "version"
