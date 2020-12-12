from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from dotenv import load_dotenv
import os
import logging
from app.models.DTOs import TeachDto

load_dotenv()

logging.basicConfig(level=logging.INFO)


def make_bot():
    bot = ChatBot(
        'Italk',
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace'
        ],
        storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
        database_uri=os.getenv('DB_CONNECTION_STRING'),
        logic_adapters=[
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.TimeLogicAdapter',
            'chatterbot.logic.BestMatch',
        ],
    )

    return bot


def train_bot(dto: TeachDto):
    trainer = ListTrainer(make_bot())
    trainer.train([
        dto.message,
        dto.response
    ])

    return trainer


def get_response(message: str):
    bot = make_bot()
    return bot.get_response(message)
