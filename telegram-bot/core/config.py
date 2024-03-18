from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class UserRoles:
    dispatcher_role: int  # Токен для доступа к телеграм-боту
    master_role: int
    operator_role: int
    director_role: int


@dataclass
class Config:
    tg_bot: TgBot
    # db: DatabaseConfig
    # roles: UserRoles


def load_config(path: str | None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))),
        # db=DatabaseConfig(
        #     database=env('DATABASE'),
        #     db_host=env('DB_HOST'),
        #     db_user=env('DB_USER'),
        #     db_password=env('DB_PASSWORD'),
        #     db_dbname=env('DB_DATABASE_NAME'),
        #     db_port=env('DB_PORT')),
        # roles=UserRoles(
        #     dispatcher_role=env('DISPATCHER_ROLE'),
        #     master_role=env('MASTER_ROLE'),
        #     operator_role=env('OPERATOR_ROLE'),
        #     director_role=env('DIRECTOR_ROLE'))
    )
