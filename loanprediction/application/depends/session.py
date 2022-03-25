from fastapi import Cookie
from loanprediction.infrastructure.sessions import Session, SessionsHolder


def get_session(session_id: str = Cookie(None)) -> Session:
    print("cookei", session_id)
    return SessionsHolder.get_session(session_id)
