from fastapi import Depends, HTTPException , status
from sqlalchemy.orm import Session
from app.schemas.user import User
from app.models.user import UserModel

from app.services.user_service import get_user_by_email , create_user
from app.utils.password_handler import get_password_hash , verify_password
from app.utils.jwt_handler import create_access_token

def signup(user : UserModel, db: Session) :
    existing_user = get_user_by_email(user.email, db)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    hashed_password = get_password_hash(user.password)
    user = UserModel(
        first_name=user.first_name,
        last_name=user.last_name,
        email = user.email,
        password=hashed_password)
    return create_user(user , db)


def login_User(email : str, password : str, db: Session) :
    user = get_user_by_email(email,db)
    if not user or not verify_password(password,user.password) :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(
        data ={"sub" : user.first_name+ "_" +user.last_name },  role="user"
    )
    
    return {"access_token" : token, "token_type" : "bearer"}


 