from loanprediction.infrastructure.exceptions.base_exception import (
    BaseInfrastructureException,
)


class SessionNotExist(BaseInfrastructureException):
    message = "Session does not exist for this user"
