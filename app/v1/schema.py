"""Pydantic models input and output to routes"""
import enum
from pydantic import BaseModel


class TaskOptStatus(str, enum.Enum):
    """Possible status of a task in the application"""

    RUNNING = "Running"
    NOT_FOUND = "Not found"
    FINISHED = "Finished"


class IdModel(BaseModel):
    """Base id model"""

    id: int


class TaskModel(IdModel):
    """Base model for task"""

    status: TaskOptStatus


class TaksCountModel(BaseModel):
    """Model to output, number of tasks running"""

    total_running: int


class DetailsErrorModel(BaseModel):
    """Detail model of exceptions"""

    description: str
    traceback: str


class InternalErrorModel(BaseModel):
    """Internal error model to responses"""

    detail: DetailsErrorModel


class HealthStatusModel(BaseModel):
    """Model for health status, ideally
    it should be created with enum if it has more status"""

    status: str


class CredentialDetailModel(BaseModel):
    """Data model for detail when unauthenticated"""

    authenticated: bool
    message: str


class AuthExecptionModel(BaseModel):
    """ "Data model when x-apikey is invalid"""

    detail: CredentialDetailModel
