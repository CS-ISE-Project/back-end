from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import User
from app.models.user import UserModel


def get_all_users(db: Session) :
    return db.query(User).all()

def get_user(user_id: int , db : Session):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(user_email: str , db: Session) :
    return db.query(User).filter(User.email == user_email).first()


def create_user(user: UserModel , db: Session) :
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email = user.email,
        password = user.password)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# TODO : A better solution to do is to separate the password modification from the update endpoint
def update_user(user_id : int , updated_user : UserModel , db: Session) : 
    db_user = db.query(User).filter(User.id == user_id).first()
    
    db_user.first_name=updated_user.first_name,
    db_user.last_name=updated_user.last_name,
    db_user.email = updated_user.email,
    db_user.password = updated_user.password
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(user_id : int , db : Session) :
    db_user = db.query(User).filter(User.id == user_id).first()
    
    db.delete(db_user)
    db.commit()
    return db_user