from fastapi import FastAPI
import logging
from sqlalchemy import inspect
from app.models.base import Base
from app.config import engine, SessionLocal
from app.routes import auth, user, role, task, task_status, task_type

# Import models to resolve dependency issue
from app.models.role import Role
from app.models.user import User
from app.models.task_status import TaskStatus
from app.models.task_type import TaskType
from app.models.task_status import TaskStatus
from app.models.task import Task
from app.utils.seeder import seed_data

# Initialize database
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="PMT", version="1.0.0")

# Create tables and seed data
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)  # Create tables
    db = SessionLocal()
    
    inspector = inspect(engine)
    logging.info(f"Existing tables: {inspector.get_table_names()}")
    
    try:
        seed_data(db)
    finally:
        db.close()

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(role.router, prefix="/user_roles", tags=["User Roles"])
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])
app.include_router(task_status.router, prefix="/tasks_status", tags=["Tasks Status"])
app.include_router(task_type.router, prefix="/tasks_type", tags=["Tasks Type"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the PMT!"}
