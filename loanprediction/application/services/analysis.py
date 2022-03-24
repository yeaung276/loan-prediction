from fastapi import APIRouter

analysisServices = APIRouter(prefix="/analysis")


@analysisServices.post("/upload_csv")
async def upload_csv() -> str:
    return "csv_uploaded"
