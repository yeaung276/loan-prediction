from typing import Any, Dict
import pandas as pd
from fastapi import APIRouter, UploadFile
from application.depends.cookies import get_session, get_session_mock
from application.responses import GraphResponse, Response, NotFound
from core.Exception import ColumnNotFound
from core.Service.visualization import Visualizer

analysisServices = APIRouter(prefix="/analysis", tags=["analysis"])


@analysisServices.post("/upload_csv/{session_id}")
async def upload_csv(session_id: str, file: UploadFile) -> Response:
    session = get_session_mock(session_id)
    session.save(Visualizer(pd.read_csv(file.file)))
    return Response(
        content={
            "sessionId": session_id,
            "filename": file.filename,
        },
    )


@analysisServices.get("/graph_null")
def graph_null(session_id: str) -> GraphResponse:
    session = get_session_mock(session_id)
    visualizer = session.get()
    graph = visualizer.graph_null().export()
    return GraphResponse(graph)


@analysisServices.get("/graph_column/{column}")
def graph_column(column: str, session_id: str) -> GraphResponse:
    session = get_session_mock(session_id)
    visualizer = session.get()
    try:
        graph = visualizer.graph_column(column).export()
        return GraphResponse(graph)
    except ColumnNotFound as error:
        raise NotFound(error.message) from error


@analysisServices.get("/columns")
def get_columns(session_id: str) -> dict:
    session = get_session_mock(session_id)
    visualizer = session.get()
    return {"columns": visualizer.get_columns()}


@analysisServices.get("/info")
def get_info() -> Any:
    # session = get_session_mock(session_id)
    visualizer = Visualizer(pd.read_csv("data/train_.csv"))
    return visualizer.get_data_info()
