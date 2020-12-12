from chatterbot import ChatBot
import os
import logging

logging.basicConfig(level=logging.INFO)

bot = ChatBot(
    'Italk',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
    ],
    database_uri=os.getenv('DB_CONNECTION_STRING')
)
