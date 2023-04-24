from dataclasses import dataclass

from environs import Env


@dataclass
class Config:
    TOKEN: str
    GROUP_ID: int
    LIVE_CHAT_ID: int


def load_config() -> Config:
    env = Env()
    env.read_env()

    return Config(
        TOKEN=env.str("TOKEN"),
        GROUP_ID=env.int("GROUP_ID"),
        LIVE_CHAT_ID=env.int("LIVE_CHAT_ID"),
    )
