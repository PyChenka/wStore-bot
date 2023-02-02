from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.utils import exceptions

from init_bot import bot
from keyboards import buttons_client


# @dp.message_handler(commands=['start', 'help'])
async def welcome_send(message: Message):
    """Отправляет приветственное сообщение и подсказку по навигации"""
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать в студию Windstore!\n\n'
                                                     'Смотреть магазин: /shop\n'
                                                     'Перейти на сайт: /site',
                               reply_markup=buttons_client)
    except exceptions.CantInitiateConversation:
        await message.reply('Постучитесь к чат-боту, чтобы продолжить: \nhttps://t.me/w_store_bot')


# @dp.message_handler(commands=['shop'])
async def show_available_pieces(message: Message):
    """Показывает товары в наличии"""
    pass


# @dp.message_handler(commands=['site'])
async def show_website(message: Message):
    """Отправляет ссылку на веб-сайт"""
    await bot.send_message(message.from_user.id, 'https://inspireuplift.com/shop/windstoretextiles')


def register_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(welcome_send, commands=['start', 'help'])
    dp.register_message_handler(show_available_pieces, commands=['shop'])
    dp.register_message_handler(show_website, commands=['site'])