from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_load = KeyboardButton('/load')
button_delete = KeyboardButton('/delete')

buttons_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons_admin.row(button_load, button_delete)