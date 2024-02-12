from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db
from schemas import User
from service import TaskService, UserService, TimesheetService

def initiate_task_service(
    db: Session = Depends(get_db),
):
    return TaskService(db=db)


def initiate_user_service(
    db: Session = Depends(get_db),
):
    return UserService(db=db)


def initiate_timesheet_service(
    db: Session = Depends(get_db),
):
    return TimesheetService(db=db)
