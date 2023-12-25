from sqlalchemy.orm import Session
from uuid import UUID
from crud import TimesheetCRUD, UserCRUD, TaskCRUD
from exceptions import GeneralException
import schemas as schemas


class UserService:
    def __init__(self, db: Session):
        self.crud = UserCRUD(db)

    def create_user(self, data: schemas.UserCreate):
        return self.crud.create_user(username=data.username)


class TaskService:
    def __init__(self, db: Session):
        self.crud = TaskCRUD(db)

    def create_task(self):
        return self.crud.create_task()


class TimesheetService:
    def __init__(
        self, requesting_user: schemas.User, db: Session,
    ) -> None:

        self.crud = TimesheetCRUD(db)

        if requesting_user is None:
            raise GeneralException("Requesting User was not provided.")

    def clock_in(self, data: schemas.TimesheetCreate):
        result = self.crud.create_timesheet(task_id=data.task_id, user_id=data.user_id)
        return result

    def clock_out(self, task_id: UUID, data: schemas.TimesheetClockOut):
        result = self.crud.update_timesheet(task_id=task_id, user_id=data.user_id)
        return result

    def get_user_timesheets(self, user_id: UUID):
        return self.crud.get_user_timesheets(user_id=user_id)

    def get_task_timesheets(self, task_id: UUID):
        return self.crud.get_task_timesheets(task_id=task_id)

    def get_task_timesheet(self, task_id: UUID, user_id: UUID):
        return self.crud.get_task_timesheet(task_id=task_id, user_id=user_id)