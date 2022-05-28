from typing import Dict
import uuid
from loanprediction.core.Service.visualization import Visualizer

from loanprediction.infrastructure.exceptions.sessions_exception import (
    SessionNotExist,
    SessionNotInitialized,
)


class SessionsHolder:
    __sessions: Dict[str, "Session"] = {}

    @classmethod
    def has_session(cls, key: str) -> bool:
        return key in cls.__sessions

    @classmethod
    def get_session(cls, key: str) -> "Session":
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
        self.visualizer = None

    def save(self, visualizer: Visualizer) -> None:
        self.visualizer = visualizer

    def get(self) -> Visualizer:
        if self.visualizer is None:
            raise SessionNotInitialized
        return self.visualizer
