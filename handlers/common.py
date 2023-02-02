import json
import string

from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from keyboards import button_ok


# @dp.message_handler()
async def echo_send(message: types.Message):
    """Фильтрует ругательства и отвечает на приветствие"""
    if {word.lower().translate(str.maketrans('', '', string.punctuation)) for word in message.text.split(' ')}\
        .intersection(set(json.load(open('mat.json')))):
        await message.reply('Ругаться здесь нельзя!')
        await message.answer('Больше не будем?', reply_markup=button_ok)
        await message.delete()

    if message.text == 'Привет':
        await message.answer('Приветик)')
        # await message.reply(message.text)
        # await bot.send_message(message.from_user.id, message.text)

    if message.text == 'OK':
        await message.answer('Хорошо!', reply_markup=ReplyKeyboardRemove())


def reg_handlers_common(dp: Dispatcher):
    dp.register_message_handler(echo_send)
