"""Global Exceptions"""
from typing import Any
from fastapi import HTTPException, status

ACTION_FORBIDDEN_MESSAGE = "You are not allowed to perform this request"


class GeneralException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class BaseNotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class BaseConflictException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


class BaseForbiddenException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


def handle_bad_request_exception(exception: Exception):
    """Raises an 400 HTTPException"""

    raise HTTPException(
        detail=str(exception), status_code=status.HTTP_400_BAD_REQUEST
    ) from exception


def handle_not_found_exception(exception: Exception):
    """Raises an 404 HTTPException"""

    raise HTTPException(
        detail=str(exception), status_code=status.HTTP_404_NOT_FOUND
    ) from exception


def handle_conflict_exception(exception: Exception):
    """Raises an 409 HTTPException"""

    raise HTTPException(
        detail=str(exception), status_code=status.HTTP_409_CONFLICT
    ) from exception


def handle_forbidden_exception(exception: Exception):
    """Raises an 403 HTTPException"""

    raise HTTPException(
        detail=str(exception), status_code=status.HTTP_403_FORBIDDEN
    ) from exception

