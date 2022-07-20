from infrastructure.exceptions.base_infra_exception import (
    BaseInfrastructureException,
)


class SessionNotExist(BaseInfrastructureException):
    message = "Session does not exist for this user"


class SessionNotInitialized(BaseInfrastructureException):
    message = "Excel data does not exist on this session yet"
