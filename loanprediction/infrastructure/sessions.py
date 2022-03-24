import uuid

from loanprediction.infrastructure.exceptions.sessions_exception import SessionNotExist


class SessionsHolder:
    __sessions: dict = {}

    @classmethod
    def has_session(cls, key: str) -> bool:
        return key in cls.__sessions

    @classmethod
    def get_session(cls, key: str) -> object:
        try:
            return cls.__sessions[key]
        except KeyError as error:
            raise SessionNotExist from error

    @classmethod
    def delete_session(cls, key: str) -> None:
        try:
            del cls.__sessions[key]
        except KeyError as key_error:
            raise SessionNotExist from key_error

    @classmethod
    def add_session(cls, session: "Session") -> str:
        cls.__sessions[session.key] = session
        return session.key


class Session:
    def __init__(self) -> None:
        self.key = str(uuid.uuid4())
