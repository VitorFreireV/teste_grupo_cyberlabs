
"""
    Implement routes to queue. Add new tasks and check status
"""
import asyncio
import traceback
from fastapi import APIRouter, Depends, Request, status as status_code
from fastapi.responses import JSONResponse
from app.v1.exception_handlers import InternalErrorException
from app.v1.helper import is_working, log_error, simple_task
from app.v1 import schema
from app.v1.auth import validate_token
from app.config import SETTINGS


TASKS_ID_COUNT = {"id":0}
TASKS_MAP = {}

router = APIRouter(
    prefix="/queue",
    tags=["queue"],
    responses={status_code.HTTP_404_NOT_FOUND: {"detail": "Not found"}},
)


@router.patch("/is_working")
async def add_client_apk_classification(request: Request):
    if await is_working():
        return JSONResponse([True], status_code.HTTP_404_NOT_FOUND)


@router.post(
    "/tasks",
    responses={
        status_code.HTTP_201_CREATED: {
            "model": schema.IdModel,
            "description": "Task was created successfully.",
        },
        status_code.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": schema.InternalErrorModel,
            "description": "Internal server error",
        },
    },
)
async def create_task(response: JSONResponse, token: str = Depends(validate_token)):
    """ Create a new Taks and save id : Task object in TASKS_MAP """
    try:
        response.status_code = status_code.HTTP_201_CREATED
        TASKS_ID_COUNT["id"] += 1
        TASKS_MAP[TASKS_ID_COUNT["id"]] = asyncio.create_task(
            simple_task(TASKS_ID_COUNT["id"]), name=TASKS_ID_COUNT["id"]
        )
        return schema.IdModel(id=TASKS_ID_COUNT["id"])
    except:
        details = traceback.format_exc()
        await log_error("create_task", details=details)
        raise InternalErrorException(
            detail={"description": "Internal server error", "traceback": details}
        )


@router.get(
    "/tasks",
    responses={
        status_code.HTTP_200_OK: {
            "model": schema.TaksCountModel,
            "description": "Success, 'total_running' contains the tasks number in Running state.",
        },
        status_code.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": schema.InternalErrorModel,
            "description": "Internal server error",
        },
    },
)
async def count_running_tasks(
    token: str = Depends(validate_token)
):
    """
    Count number of tasks in Running
    canceled status can be useful in other scenarios
    in this case, let's assume that no task can be canceled
    """
    try:
        active_tasks = sum([not tk.done() for tk in TASKS_MAP.values()])
        return schema.TaksCountModel(total_running=active_tasks)
    except:
        details = traceback.format_exc()
        await log_error("count_tasks", details=details)
        raise InternalErrorException(
            detail={"description": "Internal server error", "traceback": details}
        )


@router.get(
    "/tasks/{id}",
    responses={
        status_code.HTTP_200_OK: {
            "model": schema.TaskModel,
            "description": "Success, 'count' contains the tasks number in state.",
        },
        status_code.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": schema.InternalErrorModel,
            "description": "Internal server error",
        },
    },
)
async def get_task_status(
    id: int, token: str = Depends(validate_token)
):
    """ return status by task id """
    try:
        if id in TASKS_MAP:
            status = "Finished" if TASKS_MAP[id].done() else "Running"
        else:
            status = "Not found"
        return schema.TaskModel(id=id, status=status)
    except:
        details = traceback.format_exc()
        await log_error("get_task_status", details=details)
        raise InternalErrorException(
            detail={"description": "Internal server error", "traceback": details}
        )
