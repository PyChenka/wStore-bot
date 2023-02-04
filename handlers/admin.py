from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from database.sqlite_db import db_add, db_read_all, db_delete
from init_bot import bot
from keyboards import buttons_operations, buttons_delete

ID = None


class AdminLoadItem(StatesGroup):
    waiting_photo = State()
    waiting_title = State()
    waiting_description = State()
    waiting_price = State()


async def set_admin_id(message: Message):
    """Устанавливает ID текущего админа"""
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Выберите действие:', reply_markup=buttons_operations)
    await message.delete()


async def start_loading(message: Message):
    """Начало диалога загрузки нового товара"""
    if message.from_user.id == ID:
        await AdminLoadItem.waiting_photo.set()
        await message.reply('Загрузите фото товара')


async def cancel_loading(message: Message, state: FSMContext):
    """Отмена загрузки"""
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.answer('Отмена загрузки')


async def load_photo(message: Message, state: FSMContext):
    """Загрузка фото"""
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await AdminLoadItem.next()
        await message.reply('Напишите название товара')


async def load_title(message: Message, state: FSMContext):
    """Сохранение названия товара"""
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['title'] = message.text
        await AdminLoadItem.next()
        await message.answer('Введите описание')


async def load_description(message: Message, state: FSMContext):
    """Сохранение описания товара"""
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await AdminLoadItem.next()
        await message.answer('Введите цену')


async def load_price(message: Message, state: FSMContext):
    """Сохранение цены товара"""
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = message.text

        await db_add(state)
        await state.finish()


async def delete_item(message: Message):
    """Отображает товары на удаление"""
    if message.from_user.id == ID:
        items = await db_read_all()
        for item in items:
            button = InlineKeyboardButton(text=f'Удалить', callback_data=f'del {item[1]}')
            await bot.send_photo(message.from_user.id, item[0])
            await bot.send_message(message.from_user.id, text=f'{item[1]}', reply_markup=InlineKeyboardMarkup().add(button))


async def delete_run(query: CallbackQuery):
    await db_delete(query.data.replace('del ', ''))
    await query.answer(text=f'Товар удален!', show_alert=True)


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(start_loading, commands=['load'], state='*')
    dp.register_message_handler(cancel_loading, commands=['cancel'], state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=AdminLoadItem.waiting_photo)
    dp.register_message_handler(load_title, state=AdminLoadItem.waiting_title)
    dp.register_message_handler(load_description, state=AdminLoadItem.waiting_description)
    dp.register_message_handler(load_price, state=AdminLoadItem.waiting_price)
    dp.register_message_handler(set_admin_id, commands=['admin'], is_chat_admin=True)
    dp.register_message_handler(delete_item, commands=['delete'])
    dp.register_callback_query_handler(delete_run, lambda x: x.data and x.data.startswith('del '))