from fastapi import Depends, HTTPException , status

from sqlalchemy.orm import Session

from app.models.user import UserModel
from app.models.admin import AdminModel
from app.models.moderator import ModeratorModel

from app.services.admin_service import get_admin_by_email, create_admin
from app.services.moderator_service import get_moderator_by_email, create_moderator
from app.services.user_service import get_user_by_email, create_user

from app.utils.hash import get_password_hash, verify_password
from app.utils.jwt import create_access_token

## ********************************** USER **********************************

def signup_user(user: UserModel, db: Session):
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

def login_user(email: str, password: str, db: Session) :
    user = get_user_by_email(email,db)
    if not user or not verify_password(password,user.password) :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(
        data ={"id" : user.id , "sub" : user.first_name+ " " +user.last_name },  role="user"
    )
    
    return {"access_token" : token, "token_type" : "bearer"}

## ************************************* ADMIN **********************************

def signup_admin(admin: AdminModel, db: Session) :
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
    return create_admin(admin, db)

def login_admin(email: str, password: str, db: Session):
    admin = get_admin_by_email(email,db)
    if not admin or not verify_password(password,admin.password) :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(
        data ={"id": admin.id , "sub": admin.first_name+ " " +admin.last_name },  role="admin"
    )
    
    return {"access_token" : token, "token_type" : "bearer"}

## ************************************* MODERATOR **********************************

def signup_moderator(mod: ModeratorModel, db: Session):
    existing_mod = get_moderator_by_email(mod.email, db)
    if existing_mod:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    hashed_password = get_password_hash(mod.password)
    mod = ModeratorModel(
        first_name=mod.first_name,
        last_name=mod.last_name,
        email = mod.email,
        password=hashed_password)
    return create_moderator(mod , db)

def login_moderator(email: str, password: str, db: Session) :
    mod = get_moderator_by_email(email,db)
    if not mod or not verify_password(password,mod.password) :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(
        data ={"id": mod.id, "sub": mod.first_name+ " " + mod.last_name},  role="moderator"
    )
    
    return {"access_token" : token, "token_type" : "bearer"}
