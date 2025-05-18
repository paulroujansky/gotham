"""
This file contains the configuration for the Gotham API.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from gotham.utils import get_package_version

# Load .env file from project root
env_path = Path(__file__).parents[2] / ".env"
load_dotenv(env_path)


class Settings:

    # Directory settings
    ROOT_DIR: Path = Path(__file__).parents[2]

    # Package settings
    package_name: str = "gotham"
    package_version: str = get_package_version(package_name)

    # Database settings
    DB_NAME: str = os.getenv("DB_NAME", "postgresDB")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASS: str = os.getenv("DB_PASS", "password")
    DB_PORT: str = os.getenv("DB_PORT", "5455")

    # SQL directory
    SQL_DIR: Path = Path(ROOT_DIR) / "src" / "gotham" / "sql"

    # Application settings
    APP_TITLE: str = "Gotham"
    APP_DESCRIPTION: str = "A Robyn-based API for managing crimes"
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", "8080"))

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
