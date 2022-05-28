from fastapi import status, HTTPException


class NotFound(HTTPException):
    def __init__(self, message: str) -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)
