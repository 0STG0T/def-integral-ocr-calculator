import asyncio
import logging

from aiogram import Bot, Dispatcher

from core.config import Config, load_config
from handlers import handlers
from aiogram.fsm.storage.memory import MemoryStorage

storage = MemoryStorage()

logging.basicConfig(level=logging.INFO)
config: Config = load_config('.env')

bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp: Dispatcher = Dispatcher(storage=storage)

dp.include_router(admin_handlers.router_admin)
dp.include_router(user_handlers.router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
