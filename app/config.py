"""
    use .env to set environment variables
    or export the variable to the environment manually
"""
from pydantic import BaseSettings, ValidationError
import dotenv


class Settings(BaseSettings):
    """Base settings from application"""

    app: dict = {}
    fastapi: dict = {}
    tasks_map: dict = {}
    harded_apikey: str
    tasks_id_count: int = 0
    app_title: str
    app_description: str
    app_version: str

    class Config:
        """Path to environment variables file"""

        env_file = ".env"


def set_env():
    """ "
    Preferably upload secret environment variables through services with AWS Secret Manager.
    Here I will implement hardcoded, simulating development environment.
    """
    dotenv.set_key(".env", "harded_apikey", "a7f9fa60-992d-4fb9-9f53-e8b1981ad418")
    dotenv.set_key(".env", "app_title", "Dev Tasks Teste")
    dotenv.set_key(".env", "app_description", "Test backend developer PSafe")
    dotenv.set_key(".env", "app_version", "0.0.0.1")


def init_settings() -> Settings:
    """if necessary, set .env"""
    try:
        return Settings()
    except ValidationError as err:
        print(str(err))
        set_env()
    finally:
        return Settings()


SETTINGS = init_settings()
