from pydantic import BaseModel
from typing import Optional


class TeachDto(BaseModel):
    message: str
    response: str


class AnswerDto(BaseModel):
    response: str


class Response(BaseModel):
    success: bool
    data: Optional[BaseModel] = None
    message: Optional[str] = ''
