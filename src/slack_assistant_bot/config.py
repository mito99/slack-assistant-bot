import os
from pathlib import Path
from time import time
from typing import List, Union

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """アプリケーション設定"""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    slack_bot_token: str
    slack_app_token: str
    slack_signing_secret: str
    log_level: str = "INFO"
    storage_path: Path = Path("./storage")
    startup_time: float = time()
    allowed_user: str


def load_config() -> Config:
    """環境変数から設定を読み込みます。"""
    return Config()