from aiogram import Bot, Dispatcher
from handlers import user
from config import TOKEN
from admin import admin
import asyncio

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(user)
    dp.include_router(admin)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print('Бот запущен.')
        asyncio.run(main())

    except KeyboardInterrupt:
        print('Бот выключен.')