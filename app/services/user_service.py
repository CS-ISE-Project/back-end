from sqlalchemy.orm import Session
from app.schemas.user import User
from app.models.user import UserModel
from app.scripts.database.setup import SessionLocal

def create_user(user: UserModel, db: Session = SessionLocal()):
    db_user = User(id=user.id, username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(user_id: int, db: Session = SessionLocal()):
    return db.query(User).filter(User.id == user_id).first()