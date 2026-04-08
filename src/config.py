from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

_ROOT = Path(__file__).resolve().parent.parent
_SRC = Path(__file__).resolve().parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(_ROOT / ".env", _SRC / ".env"),
        extra="ignore",
        env_file_encoding="utf-8",
    )

    database_url: str = "sqlite:///./blog.db"
    environment: str = "production"


settings = Settings()
