from fastapi import APIRouter, HTTPException, status
from loanprediction.application.response import Response
from loanprediction.infrastructure.exceptions.sessions_exception import SessionNotExist
from loanprediction.infrastructure.sessions import Session, SessionsHolder

sessionServices = APIRouter(prefix="/session")


@sessionServices.get("/start_session")
async def start_session() -> Response:
    new_session = Session()
    SessionsHolder.add_session(new_session)
    return Response(status=status.HTTP_200_OK, data=new_session.key)


@sessionServices.get("/stop_session/{session_id}")
async def stop_session(session_id: str) -> Response:
    try:
        SessionsHolder.delete_session(session_id)
    except SessionNotExist as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=error.message
        ) from error
    return Response(status=status.HTTP_200_OK, data="session ended")
