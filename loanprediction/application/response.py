from io import BytesIO
from typing import Any
from starlette.responses import JSONResponse as BaseResponse
from fastapi import status
from fastapi.responses import Response as FResponse


class Response(BaseResponse):
    pass


class MediaResponse(FResponse):
    def __init__(self, content: BytesIO, media_type: str = "image/png") -> None:
        super().__init__(
            status_code=status.HTTP_200_OK,
            content=content.read(),
            media_type=media_type,
        )
