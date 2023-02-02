import os
from aiogram import Bot, Dispatcher

token = os.getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot)