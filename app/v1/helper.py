"""Implement utils functions to app"""
import traceback
import asyncio
import aiologger
from app.v1.exception_handlers import InternalErrorException

logger = aiologger.Logger.with_default_handlers(level=10)


async def is_working():
    """?"""
    return True


async def log_info(func_name, description="", details=""):
    """Async logging info, structure the data as needed"""
    logger.info(f"[{func_name}]\nDESCRIPTION: {description}\nDETAILS: {details}")


async def log_error(func_name, description="", details=""):
    """Async logging error, structure the data as needed"""
    logger.error(f"[{func_name}]\nDESCRIPTION: {description}\nDETAILS: {details}")


async def simple_task(id):
    """Create a simple task"""
    try:
        await asyncio.sleep(10)
    except InternalErrorException:
        details = traceback.format_exc()
        await log_error("simple_task", details=details, description=f"task_id: {id}")
        raise InternalErrorException(
            detail={"description": "Internal server error", "traceback": details}
        )
