from fastapi import APIRouter, Depends, HTTPException, status
import loanprediction.config as config
from loanprediction.application.depends.session import get_session
from loanprediction.application.response import Response
from loanprediction.infrastructure.exceptions.sessions_exception import SessionNotExist
from loanprediction.infrastructure.sessions import Session, SessionsHolder

sessionServices = APIRouter(prefix="/session", tags=["session"])


@sessionServices.get("/start_session")
async def start_session() -> Response:
    new_session = Session()
    SessionsHolder.add_session(new_session)
    response = Response(
        status_code=status.HTTP_200_OK, content={"data": "Session created"}
    )
    response.set_cookie(config.cookie_name, new_session.key, max_age=400)
    return response


@sessionServices.get("/stop_session")
async def stop_session(session: Session = Depends(get_session)) -> Response:
    try:
        SessionsHolder.delete_session(session.key)
    except SessionNotExist as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=error.message
        ) from error
    response = Response(
        status_code=status.HTTP_200_OK, content={"data": "Session ended"}
    )
    response.delete_cookie(config.cookie_name)
    return response
