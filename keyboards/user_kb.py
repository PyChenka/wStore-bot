from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

# кнопочки надпись=команда
b1 = KeyboardButton('/shop')
b2 = KeyboardButton('/site')
b3 = KeyboardButton('OK')

# замещает клавиатуру кнопочками
# выравнивание по шрифту
# сворачивает клаву после нажатия на кнопочку
buttons_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

# кнопочки распределены по строке, еще add(b1).add(b2) - в столбик, insert - добавление в строку
buttons_client.row(b1, b2)

button_ok = ReplyKeyboardMarkup(resize_keyboard=True)
button_ok.add(b3)