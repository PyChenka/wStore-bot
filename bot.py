from aiogram.utils import executor
from init_bot import dp
from handlers import client, admin, common


async def on_startup(_):
    print('Бот активен')

# регистрация хэндлеров, когда бот разбит по файлам
client.reg_handlers_client(dp)
common.reg_handlers_common(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)