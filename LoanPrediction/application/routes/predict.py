from fastapi import APIRouter
from LoanPrediction.application.requests.predict_data import Record
from LoanPrediction.application.responses.response import Response
from LoanPrediction.core.Service.estimation import Estimator

predictionServices = APIRouter(prefix="/prediction", tags=["prediction"])


@predictionServices.post("/get_prediction")
def get_prediction(record: Record) -> Response:
    predictionService = Estimator()
    result = predictionService.predict(record)
    return Response(result.dict())
