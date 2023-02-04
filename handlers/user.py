from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.utils import exceptions

from database.sqlite_db import db_read_single
from init_bot import bot
from keyboards import buttons_menu, buttons_url


async def welcome_send(message: Message):
    """Отправляет приветственное сообщение и подсказку по навигации"""
    try:
        await bot.send_message(message.from_user.id, 'Добро пожаловать в студию Windstore!\n\n'
                                                     'Смотреть магазин: /shop\n'
                                                     'Перейти на сайт: /site',
                               reply_markup=buttons_menu)
    except exceptions.CantInitiateConversation:
        await message.reply('Постучитесь к чат-боту, чтобы продолжить: \nhttps://t.me/w_store_bot')


async def show_available_pieces(message: Message):
    """Показывает товары в наличии"""
    await db_read_single(message)


async def show_website(message: Message):
    """Отправляет ссылку на веб-сайт"""
    await bot.send_message(message.from_user.id, 'Ссылки на наши вебсайты:', reply_markup=buttons_url)


def register_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(welcome_send, commands=['start', 'help'])
    dp.register_message_handler(show_available_pieces, commands=['shop'])
    dp.register_message_handler(show_website, commands=['site'])