from fastapi import APIRouter, Body, Query
from app.models.DTOs import TeachDto, Response, AnswerDto
from app.services.chatbot.chatterbot import train_bot, get_response

router = APIRouter()


@router.get('/answer')
async def get_answer(message: str = Query(...)):
    answer = get_response(message)
    res = Response(success=True, data=AnswerDto(response=answer.text))
    return res


@router.post('/teach', response_model=Response)
async def teach(dto: TeachDto = Body(...,embed=False)):
    train_bot(dto)
    res = Response(success=True, data=dto)
    return res
