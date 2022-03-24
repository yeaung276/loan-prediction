from typing import Any
from pydantic import BaseModel


class Response(BaseModel):
    status: int
    data: Any
