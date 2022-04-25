import pytest
from app.config import SETTINGS
from app.v1.schema import IdModel, TaksCountModel, TaskModel
from fastapi import status


BASE_URL = "/queue/tasks"


@pytest.mark.asyncio
async def test_create_task(client):
    response = await client.post(
        f"{BASE_URL}", headers={"x-apikey": SETTINGS.harded_apikey}
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json().keys() == IdModel.__fields__.keys()


@pytest.mark.asyncio
async def test_count_running_task(client):
    await client.post(f"{BASE_URL}", headers={"x-apikey": SETTINGS.harded_apikey})
    await client.post(f"{BASE_URL}", headers={"x-apikey": SETTINGS.harded_apikey})
    response = await client.get(
        f"{BASE_URL}", headers={"x-apikey": SETTINGS.harded_apikey}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json().keys() == TaksCountModel.__fields__.keys()
    assert response.json()["total_running"] >= 2


@pytest.mark.asyncio
async def test_task_by_id(client):
    response = await client.post(
        f"{BASE_URL}", headers={"x-apikey": SETTINGS.harded_apikey}
    )
    task_id = response.json()["id"]
    response = await client.get(
        f"{BASE_URL}/{task_id}", headers={"x-apikey": SETTINGS.harded_apikey}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json().keys() == TaskModel.__fields__.keys()
    assert response.json()["status"] == "Running"
