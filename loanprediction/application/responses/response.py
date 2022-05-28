from io import BytesIO
from fastapi import status
from starlette.responses import JSONResponse as BaseResponse
from fastapi.responses import Response as FResponse


class Response(BaseResponse):
    def __init__(self, content: dict) -> None:
        super().__init__(status_code=status.HTTP_200_OK, content=content)


class GraphResponse(FResponse):
    def __init__(self, content: BytesIO) -> None:
        super().__init__(
            status_code=status.HTTP_200_OK,
            content=content.read(),
            media_type="image/png",
        )
