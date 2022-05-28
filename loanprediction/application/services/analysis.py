import pandas as pd
from fastapi import APIRouter, UploadFile, status
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


@analysisServices.get("/graph_null")
def graph_null(session_id: str) -> MediaResponse:
    session = get_session_mock(session_id)
    visualizer = session.get()
    graph = visualizer.graph_null().export()
    return MediaResponse(graph)
