from fastapi import Cookie, HTTPException, status
from loanprediction.infrastructure.exceptions.sessions_exception import SessionNotExist
from loanprediction.infrastructure.sessions import Session, SessionsHolder


def get_session(session_id: str = Cookie(None)) -> Session:
    print("cookei", session_id)
    return SessionsHolder.get_session(session_id)


def get_session_mock(session_id: str) -> Session:
    try:
        return SessionsHolder.get_session(session_id)
    except SessionNotExist as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=error.message
        ) from error
