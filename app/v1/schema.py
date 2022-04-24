"""Pydantic models to routes"""
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
