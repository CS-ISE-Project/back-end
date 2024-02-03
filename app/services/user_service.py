from fastapi import Depends, HTTPException, Response , status

from sqlalchemy.orm import Session

from app.schemas.user import User
from app.models.user import UserModel, UpdateUserModel

from app.utils.article import db_to_model

def get_all_users(db: Session):
    users = db.query(User).all()
    if not users : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No users found"
        )
    return users

def get_user(user_id: int, db: Session):
    user =  db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
        
    user_favorites = {}
    for favorite in user.favorites:
        article = favorite.article
        user_favorites[favorite.id] = db_to_model(article)                  
        
    return {'user': user, 'favorites': user_favorites}

def get_only_user(user_id: int, db: Session):
    user =  db.query(User).filter(User.id == user_id).first()
    if user is None :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return user
        
def get_user_by_email(user_email: str, db: Session):
    return db.query(User).filter(User.email == user_email).first()

def create_user(user: UserModel, db: Session):
    try : 
        db_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email = user.email,
            password = user.password)
    
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e: 
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the user. Error: {str(e)}"
        )
        
def update_user(user_id: int, updated_user: UpdateUserModel, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    try:
        db_user.first_name = updated_user.first_name
        db_user.last_name = updated_user.last_name
        db_user.email = updated_user.email

        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the user. Error: {str(e)}"
        )
                 
def delete_user(user_id: int, db: Session):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    try:
        db.delete(db_user)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the user. Error: {str(e)}"
        )
