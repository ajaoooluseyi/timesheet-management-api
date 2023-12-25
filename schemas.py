from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import List


class Timesheet(BaseModel):
    task_id: UUID
    user_id: UUID
    date_clocked_in: datetime
    date_clocked_out: datetime
    date_recorded: datetime


class TimesheetCreate(BaseModel):
    task_id: UUID
    user_id: UUID


class TimesheetClockOut(BaseModel):
    user_id: UUID


class TimesheetOut(BaseModel):
    timesheets: List[Timesheet]
 

class TimesheetList(TimesheetOut):
    pass


class User(BaseModel):
    id: UUID
    username: str


class UserCreate(BaseModel):
    username: str


class TaskCreate(BaseModel):
    pass  # No fields for creating a task, as it only has an ID


class Task(BaseModel):
    id: UUID

