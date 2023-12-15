from sqlalchemy.orm import Session
from app.models.user import User
from app.core.database import SessionLocal

def get_user(user_id: int):
    db = SessionLocal()
    return db.query(User).filter(User.id == user_id).first()

def create_user(user: User):
    db = SessionLocal()
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
