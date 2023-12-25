import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database import Base


class Task(Base):
    __tablename__ = "task"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)

    # Define the relationship with the Timesheet model
    timesheets = relationship("Timesheet", back_populates="task")


class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String, unique=True)

    # Define the relationship with the Timesheet model
    timesheets = relationship("Timesheet", back_populates="user")


class Timesheet(Base):
    __tablename__ = "timesheet"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    task_id = Column(UUID(as_uuid=True), ForeignKey("task.id", ondelete="CASCADE"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"))
    date_clocked_in = Column(DateTime(timezone=True), server_default=func.now())
    date_clocked_out = Column(
        DateTime(timezone=True), nullable=True, server_default=None
    )
    date_recorded = Column(DateTime(timezone=True), server_default=func.now())

    # Define the relationship with the User model
    user = relationship("User", back_populates="timesheets")

