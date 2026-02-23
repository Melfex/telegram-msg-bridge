from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    BOT_TOKEN: str
    SUDO_ID: int

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = BotSettings()
