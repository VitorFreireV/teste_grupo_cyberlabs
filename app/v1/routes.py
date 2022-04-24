from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from .helper import is_working

router = APIRouter(
    prefix="/queue",
    tags=["queue"],
    responses={404: {"detail": "Not found"}},
)


@router.patch("/is_working")
async def add_client_apk_classification(request: Request):
    if is_working():
        return JSONResponse([True], 404)
