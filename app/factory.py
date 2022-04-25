"""Centralize app instance"""
from fastapi import FastAPI
from app.config import SETTINGS
from app.v1.routes import queue, health


def create_app():
    """
    Create a app instance
    """
    app = FastAPI(
        title=SETTINGS.app_title,
        description=SETTINGS.app_description,
        version=SETTINGS.app_version,
    )
    app.include_router(queue.router)
    app.include_router(health.router)
    return app
