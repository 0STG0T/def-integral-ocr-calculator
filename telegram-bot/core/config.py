from dataclasses import dataclass
from environs import Env

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        )
    )


storage = MemoryStorage()

config: Config = load_config('.env')

bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp: Dispatcher = Dispatcher(storage=storage)
