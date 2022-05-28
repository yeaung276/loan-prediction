from fastapi import APIRouter
from loanprediction.application.routes.session import sessionServices
from loanprediction.application.routes.analysis import analysisServices

mainRouter = APIRouter()

mainRouter.include_router(sessionServices)
mainRouter.include_router(analysisServices)
