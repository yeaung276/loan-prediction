from starlette.responses import JSONResponse as BaseResponse, StreamingResponse


class Response(BaseResponse):
    pass


class MediaResponse(StreamingResponse):
    pass
