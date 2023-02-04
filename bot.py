from aiogram import Dispatcher
from aiogram.utils import executor

from database.sqlite_db import db_start
from handlers.main import register_all_handlers
from init_bot import dp


async def on_start_up(dp: Dispatcher) -> None:
    register_all_handlers(dp)
    db_start()
    print('Bot online')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
