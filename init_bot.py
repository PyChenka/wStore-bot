import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

token = os.getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)
