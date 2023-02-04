from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons = [
    KeyboardButton('/load'),
    KeyboardButton('/delete')
]

buttons_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(*buttons)
