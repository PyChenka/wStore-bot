import aiogram.utils.exceptions
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

token = os.getenv('TOKEN')
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def welcome_send(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать в студию Windstore!')
        await message.delete()
    except aiogram.utils.exceptions.CantInitiateConversation:       # если сами не писали боту
        await message.reply('Постучитесь к чат-боту, чтобы продолжить: \nhttps://t.me/w_store_bot')


# пустой обработчик должен быть в самом низу
@dp.message_handler()                                               # обрабатываются входящие сообщения
async def echo_send(message: types.Message):                        # событие - сообщение в чате
    if message.text == 'Привет':
        await message.answer('Приветик)')                           # сообщение в ответ
    # await message.reply(message.text)                             # ответ на сообщение
    # await bot.send_message(message.from_user.id, message.text)    # ответ в личку (исключение, если не писали боту)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)                   # бот не отвечает на сообщения из оффлайна