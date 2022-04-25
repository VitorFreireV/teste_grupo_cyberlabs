"""Routes to check system health"""

from fastapi import APIRouter, status as status_code
from fastapi.responses import JSONResponse
from app.v1 import schema


router = APIRouter(
    prefix="/health",
    tags=["health"],
    responses={status_code.HTTP_404_NOT_FOUND: {"detail": "Not found"}},
)


@router.get(
    "/",
    responses={
        status_code.HTTP_200_OK: {
            "model": schema.HealthStatusModel,
            "description": "Success in recovering health status.",
        },
        status_code.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": schema.InternalErrorModel,
            "description": "Internal server error",
        },
    },
)
async def check_health_status():
    """
    This function can check other application services (database, apis, routes)
    In this case, it only means that the application is online.
    """
    return JSONResponse({"status": "ok"})
