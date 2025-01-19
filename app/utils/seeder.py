from sqlalchemy.orm import Session
from app.models.role import Role
from app.models.user import User
from app.models.task_status import TaskStatus
from app.models.task_type import TaskType
from app.utils.security import hash_password

def seed_data(db: Session):
    # Seed default roles
    default_roles = [
        {"id": 1, "name": "Admin", "description": ""},
        {"id": 2, "name": "Manager", "description": ""},
        {"id": 3, "name": "User", "description": ""}
    ]
    for role in default_roles:
        if not db.query(Role).filter_by(id=role["id"]).first():
            db.add(Role(**role))
    
    # Seed default admin user
    # admin_email = "admin@example.com"
    # admin_username = "admin"
    # admin_password = hash_password("Admin@123")
    # if not db.query(User).filter_by(email=admin_email).first():
    #     db.add(User(
    #         username=admin_username,
    #         email=admin_email,
    #         password=admin_password,
    #         role_id=1  # Admin role
    #     ))
    
    # Seed task statuses
    default_statuses = [
        {"id": 1, "name": "New", "description": ""},
        {"id": 2, "name": "Active", "description": ""},
        {"id": 3, "name": "In Progress", "description": ""},
        {"id": 4, "name": "Completed", "description": ""}
    ]
    for status in default_statuses:
        if not db.query(TaskStatus).filter_by(id=status["id"]).first():
            db.add(TaskStatus(**status))
    
    # Seed task types
    default_types = [
        {"id": 1, "name": "Task", "description": ""},
        {"id": 2, "name": "Bug", "description": ""}
    ]
    for task_type in default_types:
        if not db.query(TaskType).filter_by(id=task_type["id"]).first():
            db.add(TaskType(**task_type))
    
    db.commit()
