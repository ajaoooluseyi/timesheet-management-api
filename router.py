from fastapi import APIRouter, Depends
from uuid import UUID
from service import TimesheetService, UserService, TaskService
import schemas as schemas
from database import get_db


router = APIRouter(tags=["Timesheet"], prefix="/timesheet")


@router.post("/create", response_model=schemas.User)
def create_user(data: schemas.UserCreate, user_service: UserService = Depends(get_db)):
    return user_service.create_user(data=data)


@router.post("/create-task", response_model=schemas.Task)
def create_task(task_service: TaskService = Depends(get_db)):
    return task_service.create_task()


@router.post("/clock-in", response_model=schemas.Timesheet)
def clock_in(
    data: schemas.TimesheetCreate, timesheet_service: TimesheetService = Depends(get_db)
):
    result = timesheet_service.clock_in(data=data)
    return result


@router.post("/{task_id}/clock-out", response_model=schemas.Timesheet)
def clock_out(
    task_id: UUID,
    data: schemas.TimesheetClockOut,
    timesheet_service: TimesheetService = Depends(get_db),
):
    result = timesheet_service.clock_out(task_id=task_id, data=data)
    return result


@router.get("/{user_id}", response_model=list[schemas.Timesheet])
def get_user_timesheets(
    user_id: UUID, timesheet_service: TimesheetService = Depends(get_db)
):
    result = timesheet_service.get_user_timesheets(user_id=user_id)
    return result


@router.get("/{user_id}/{task_id}", response_model=list[schemas.Timesheet])
def get_task_timesheet(
    task_id: UUID, user_id: UUID, timesheet_service: TimesheetService = Depends(get_db)
):
    result = timesheet_service.get_task_timesheet(task_id=task_id, user_id=user_id)
    return result
