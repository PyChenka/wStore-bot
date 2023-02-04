from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

buttons = [
    KeyboardButton('/load'),
    KeyboardButton('/delete'),
    InlineKeyboardButton(text='Удалить', callback_data='DATA')
]

buttons_operations = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(*buttons[:2])
buttons_delete = InlineKeyboardMarkup(row_width=1).add(*buttons[2])
