import pandas as pd
from fastapi import APIRouter, UploadFile, status, Response as FResponse
from loanprediction.application.depends.cookies import get_session_mock
from loanprediction.application.response import MediaResponse, Response
from loanprediction.core.Service.visualization import Visualizer

analysisServices = APIRouter(prefix="/analysis", tags=["analysis"])


@analysisServices.post("/upload_csv/{session_id}")
async def upload_csv(session_id: str, file: UploadFile) -> Response:
    session = get_session_mock(session_id)
    session.save(Visualizer(pd.read_csv(file.file)))
    return Response(
        status_code=status.HTTP_200_OK,
        content={
            "sessionId": session_id,
            "filename": file.filename,
        },
    )


# TODO: have to return image file correctly from api response
@analysisServices.get(
    "/graph_null",
    responses={200: {"content": {"image/png": {}}}},
    response_class=Response,
)
def graph_null() -> FResponse:
    # visualizer = Visualizer(pd.read_csv(file.file))
    visualizer = Visualizer(pd.read_csv("data/test_.csv"))
    graph = visualizer.graph_null()
    return FResponse(
        status_code=status.HTTP_200_OK, content=graph.export(), media_type="image/png"
    )
