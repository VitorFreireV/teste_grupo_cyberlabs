"""Validatation functions"""
from fastapi import Header
from app.config import SETTINGS
from app.v1.exception_handlers import CredentialsException


async def validate_token(x_apikey: str = Header(..., description="x-apikey")):
    """Validate and return user token"""
    if SETTINGS.harded_apikey == x_apikey:
        return "user_token"

    raise CredentialsException(
        detail={"authenticated": False, "message": "Unauthenticated"}
    )
