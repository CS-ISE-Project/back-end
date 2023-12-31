from fastapi import Depends, HTTPException , status
from sqlalchemy.orm import Session
from app.schemas.user import User
from app.models.user import UserModel
from app.models.moderator import ModeratorModel 
from app.models.admin import AdminModel 
from app.services.user_service import get_user_by_email , create_user
from app.services.admin_service import get_admin_by_email , create_admin
from app.utils.password_handler import get_password_hash , verify_password
from app.utils.jwt_handler import create_access_token


## ********************************** USER **********************************

def signup_User(user : UserModel , db: Session) :
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
        data ={"id" : user.id , "sub" : user.first_name+ "_" +user.last_name },  role="user"
    )
    
    return {"access_token" : token, "token_type" : "bearer"}


## ************************************* ADMIN **********************************

def signup_Admin(admin : AdminModel , db: Session) :
    existing_admin = get_admin_by_email(admin.email, db)
    if existing_admin:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    hashed_password = get_password_hash(admin.password)
    admin = AdminModel(
        first_name=admin.first_name,
        last_name=admin.last_name,
        email = admin.email,
        password=hashed_password)
    return create_admin(admin , db)


def login_Admin(email : str, password : str, db: Session) :
    admin = get_admin_by_email(email,db)
    if not admin or not verify_password(password,admin.password) :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(
        data ={"id" : admin.id , "sub" : admin.first_name+ "_" +admin.last_name },  role="admin"
    )
    
    return {"access_token" : token, "token_type" : "bearer"}

