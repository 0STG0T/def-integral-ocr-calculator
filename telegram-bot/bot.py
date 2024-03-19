import asyncio
import logging

from aiogram import Bot, Dispatcher

from core.config import bot, dp
from handlers import handlers


logging.basicConfig(level=logging.INFO)

dp.include_router(handlers.router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
