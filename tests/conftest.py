from asgi_lifespan import LifespanManager
import pytest
from run import app
import httpx


@pytest.fixture
async def test_app():
    async with LifespanManager(app):
        yield app


@pytest.fixture
async def client(test_app):
    async with httpx.AsyncClient(app=test_app, base_url="http://test") as client:
        yield client
