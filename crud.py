from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Timesheet, User, Task
from uuid import UUID
from datetime import datetime
from exceptions import BaseConflictException, BaseNotFoundException, GeneralException


class UserCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str) -> User:
        db_user = User(username=username)
        self.db.add(db_user)

        try:
            self.db.commit()
            self.db.refresh(db_user)
            return db_user
        except Exception as e:
            self.db.rollback()
            raise BaseConflictException(e)


class TaskCRUD:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self) -> Task:
        db_task = Task()
        self.db.add(db_task)

        try:
            self.db.commit()
            self.db.refresh(db_task)
            return db_task
        except Exception as e:
            self.db.rollback()
            raise BaseConflictException(f"Failed to create task: {str(e)}")


class TimesheetCRUD:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_timesheet(self, user_id: UUID, task_id: UUID) -> Timesheet:
        try:
            db_timesheet = Timesheet(task_id=task_id, user_id=user_id)
            self.db.add(db_timesheet)
            self.db.commit()
            self.db.refresh(db_timesheet)
            return db_timesheet
        except IntegrityError:
            raise BaseConflictException("This user has already clocked in this Task.")

    def update_timesheet(
        self, user_id: UUID, task_id: UUID,
    ) -> Timesheet:
        try:
            db_timesheet = self.get_task_timesheet(task_id=task_id, user_id=user_id)
            if db_timesheet is None:
                raise BaseNotFoundException("The task does not exist.")

            if db_timesheet:
                db_timesheet.date_clocked_out = datetime.utcnow()
                self.db.commit()
                self.db.refresh(db_timesheet)
                return db_timesheet

        except Exception as raised_exception:
            raise GeneralException(str(raised_exception))

    def get_user_timesheets(self, user_id: UUID) -> list[Timesheet]:
        return self.db.query(Timesheet).filter(Timesheet.user_id == user_id).all()

    def get_task_timesheets(self, task_id: UUID) -> list[Timesheet]:
        return self.db.query(Timesheet).filter(Timesheet.task_id == task_id).all()

    def get_task_timesheet(self, task_id: UUID, user_id: UUID) -> Timesheet:
        return (
            self.db.query(Timesheet)
            .filter(Timesheet.task_id == task_id, Timesheet.user_id == user_id)
            .first()
        )
