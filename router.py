from fastapi import APIRouter, Security
from uuid import UUID
from service import TimesheetService, UserService, TaskService
import schemas as schemas
from dependencies import (
    initiate_user_service,
    initiate_task_service,
    initiate_timesheet_service,
)


router = APIRouter(tags=["Timesheet"], prefix="/timesheet")


@router.post("/create-user", response_model=schemas.User)
def create_user(
    data: schemas.UserCreate,
    user_service: UserService = Security(initiate_user_service),
):
    return user_service.create_user(data=data)


@router.post("/create-task", response_model=schemas.Task)
def create_task(task_service: TaskService = Security(initiate_task_service)):
    return task_service.create_task()


@router.post("/clock-in", response_model=schemas.Timesheet)
def clock_in(
    data: schemas.TimesheetCreate,
    timesheet_service: TimesheetService = Security(initiate_timesheet_service),
):
    result = timesheet_service.clock_in(data=data)
    return result


@router.post("/clock-out", response_model=schemas.Timesheet)
def clock_out(
    data: schemas.TimesheetClockOut,
    timesheet_service: TimesheetService = Security(initiate_timesheet_service),
):
    result = timesheet_service.clock_out(task_id=data.task_id, data=data)
    return result


@router.get("/{user_id}", response_model=schemas.TimesheetOut)
def get_user_timesheets(
    user_id: UUID,
    timesheet_service: TimesheetService = Security(initiate_timesheet_service),
):
    result = timesheet_service.get_user_timesheets(user_id=user_id)
    return result


@router.get("/{user_id}/{task_id}", response_model=schemas.Timesheet)
def get_user_task_timesheet(
    task_id: UUID,
    user_id: UUID,
    timesheet_service: TimesheetService = Security(initiate_timesheet_service),
):
    result = timesheet_service.get_user_task_timesheet(task_id=task_id, user_id=user_id)
    return result


@router.get("/{task_id}", response_model=schemas.TimesheetOut)
def get_task_timesheet(
    task_id: UUID,
    timesheet_service: TimesheetService = Security(initiate_timesheet_service),
):
    result = timesheet_service.get_task_timesheets(task_id=task_id)
    return result
