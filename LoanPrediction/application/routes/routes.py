from fastapi import APIRouter
from LoanPrediction.application.routes.session import sessionServices
from LoanPrediction.application.routes.analysis import analysisServices
from LoanPrediction.application.routes.predict import predictionServices

mainRouter = APIRouter()

mainRouter.include_router(sessionServices)
mainRouter.include_router(analysisServices)
mainRouter.include_router(predictionServices)
