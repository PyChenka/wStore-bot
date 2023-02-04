import sqlite3

from aiogram.types import Message

from init_bot import bot


def db_start():
    global base, cur
    base = sqlite3.connect('windstore_shop.db')
    cur = base.cursor()
    if base:
        print('Database connected')
    base.execute('CREATE TABLE IF NOT EXISTS shop(img TEXT, title TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def db_add(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO shop VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def db_read(message: Message):
    for item in cur.execute('SELECT * FROM shop').fetchall():
        await bot.send_photo(message.from_user.id, item[0], f'{item[1]}\n{item[2]}\n{item[3]}')