from fastapi import APIRouter
from loanprediction.application.services.session import sessionServices
from loanprediction.application.services.analysis import analysisServices

mainRouter = APIRouter()

mainRouter.include_router(sessionServices)
mainRouter.include_router(analysisServices)
