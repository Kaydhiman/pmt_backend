from sqlalchemy.orm import Session
from app.models.role import Role
from app.schemas.role import RoleCreate

def create_role(db: Session, role: RoleCreate):
    db_role = Role(name=role.name, description=role.description)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_all_roles(db: Session):
    return db.query(Role).all()

def get_role_by_id(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()

def delete_role(db: Session, role_id: int):
    role = get_role_by_id(db, role_id)
    if role:
        db.delete(role)
        db.commit()
        return True
    return False

def update_role_by_id(db: Session, role_id: int, updated_role: RoleCreate):
    role = get_role_by_id(db, role_id)
    if role:
        db.commit()
        db.refresh(updated_role)
        return True
    return False