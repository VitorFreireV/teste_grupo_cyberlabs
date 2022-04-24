from pydantic import BaseSettings



class Settings(BaseSettings):
    app: dict
    fastapi: dict