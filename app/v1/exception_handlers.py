"""Custom Exceptions"""
from fastapi import HTTPException


class CredentialsException(HTTPException):
    """Credential error"""

    def __init__(self, detail: dict, status_code: int = 401):
        self.detail = detail
        self.status_code = status_code


class InternalErrorException(HTTPException):
    """Internal Error"""

    def __init__(self, detail: dict, status_code: int = 500):
        self.detail = detail
        self.status_code = status_code
