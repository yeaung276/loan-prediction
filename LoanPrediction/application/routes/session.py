from fastapi import APIRouter, Depends
import LoanPrediction.config as config
from LoanPrediction.application.depends.cookies import get_session
from LoanPrediction.application.responses import Response, NotFound
from LoanPrediction.infrastructure.exceptions.sessions_exception import SessionNotExist
from LoanPrediction.infrastructure.sessions import Session, SessionsHolder

sessionServices = APIRouter(prefix="/session", tags=["session"])


@sessionServices.get("/start_session")
async def start_session() -> Response:
    new_session = Session()
    SessionsHolder.add_session(new_session)
    response = Response(
        content={"data": {"message": "Session created", "session": new_session.key}},
    )
    response.set_cookie(
        config.cookie_name,
        new_session.key,
        max_age=400,
        samesite="Lax",
        secure=False,
    )
    return response


@sessionServices.get("/stop_session")
async def stop_session(session: Session = Depends(get_session)) -> Response:
    try:
        SessionsHolder.delete_session(session.key)
    except SessionNotExist as error:
        raise NotFound(message=error.message) from error
    response = Response(content={"data": {"message": "Session ended"}})
    response.delete_cookie(config.cookie_name)
    return response
