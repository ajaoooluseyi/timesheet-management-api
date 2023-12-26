from sqlalchemy.orm import Session
from uuid import UUID
from crud import TimesheetCRUD, UserCRUD, TaskCRUD
from exceptions import GeneralException
import schemas as schemas


class UserService:
    def __init__(self, db: Session):
        self.crud = UserCRUD(db)

    def create_user(self, data: schemas.UserCreate):
        user = self.crud.create_user(username=data.username)
        return schemas.User.parse_obj(user.__dict__)


class TaskService:
    def __init__(self, db: Session):
        self.crud = TaskCRUD(db)

    def create_task(self):
        task = self.crud.create_task()
        return schemas.Task.parse_obj(task.__dict__)


class TimesheetService:
    def __init__(
        self,
        db: Session,
    ) -> None:
        self.crud = TimesheetCRUD(db)

    def clock_in(self, data: schemas.TimesheetCreate):
        try:
            result = self.crud.create_timesheet(
                task_id=data.task_id, user_id=data.user_id
            )
            return schemas.Timesheet.parse_obj(result.__dict__)

        except Exception as raised_exception:
            raise GeneralException(str(raised_exception))

    def clock_out(self, data: schemas.TimesheetClockOut):
        try:
            result = self.crud.update_timesheet(
                task_id=data.task_id, user_id=data.user_id
            )
            return schemas.Timesheet.parse_obj(result.__dict__)
        except Exception as raised_exception:
            raise GeneralException(str(raised_exception))

    def get_user_timesheets(self, user_id: UUID):
        try:
            timesheets = self.crud.get_user_timesheets(user_id=user_id)
            total = self.crud.get_total_user_timesheets(user_id=user_id)
            return schemas.TimesheetOut.parse_obj(
                {
                    "total": total,
                    "timesheets": timesheets,
                }
            )
        except Exception as raised_exception:
            raise GeneralException(str(raised_exception))

    def get_task_timesheets(self, task_id: UUID):
        try:
            timesheets = self.crud.get_task_timesheets(task_id=task_id)
            total = self.crud.get_total_task_timesheets(task_id == task_id)
            return schemas.TimesheetOut.parse_obj(
                {
                    "total": total,
                    "timesheets": timesheets,
                }
            )
        except Exception as raised_exception:
            raise GeneralException(str(raised_exception))

    def get_user_task_timesheet(self, task_id: UUID, user_id: UUID):
        try:
            timesheet = self.crud.get_user_task_timesheet(
                task_id=task_id, user_id=user_id
            )
            return schemas.Timesheet.parse_obj(timesheet.__dict__)
        except Exception as raised_exception:
            raise GeneralException(str(raised_exception))
