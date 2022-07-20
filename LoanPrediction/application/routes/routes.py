from fastapi import APIRouter
from application.routes.session import sessionServices
from application.routes.analysis import analysisServices
from application.routes.predict import predictionServices

mainRouter = APIRouter()

mainRouter.include_router(sessionServices)
mainRouter.include_router(analysisServices)
mainRouter.include_router(predictionServices)
