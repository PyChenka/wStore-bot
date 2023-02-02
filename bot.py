from aiogram import Dispatcher
from aiogram.utils import executor

from handlers.main import register_all_handlers
from init_bot import dp


async def on_start_up(dp: Dispatcher) -> None:
    register_all_handlers(dp)
    print('Бот активен')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
