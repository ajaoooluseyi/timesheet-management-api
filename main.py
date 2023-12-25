from fastapi import FastAPI
from router import router as timesheet_router
from database import engine
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(timesheet_router)
