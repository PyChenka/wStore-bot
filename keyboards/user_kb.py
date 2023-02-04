from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

buttons = [
    KeyboardButton('/shop'),
    KeyboardButton('/site'),
    InlineKeyboardButton(text='Pinterest', url='https://ru.pinterest.com/windstoretextiles/'),
    InlineKeyboardButton(text='Instagram', url='https://instagram.com/windstoretextiles/'),
    InlineKeyboardButton(text='Website', url='https://inspireuplift.com/shop/windstoretextiles')
]

buttons_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(*buttons[:2])
buttons_url = InlineKeyboardMarkup(row_width=2).add(*buttons[2:5])
