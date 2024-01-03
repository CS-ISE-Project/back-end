from sqlalchemy.orm import Session

from app.models.user import UserModel
from app.models.admin import AdminModel
from app.models.moderator import ModeratorModel

from app.services.auth_service import signup_user, login_user, signup_admin, login_admin, signup_moderator, login_moderator

## ************************************* USER **********************************

def signup_user_controller(user: UserModel, db: Session):
    try:
        db_user = signup_user(user, db)
        return db_user
    except Exception as e:
        raise e
    
def login_user_controller(email: str, password: str, db: Session) :  
    try : 
        token = login_user(email, password, db) 
        return token
    except Exception as e : 
        raise e

## ************************************* ADMIN **********************************
    
def signup_admin_controller(admin: AdminModel, db: Session):
    try:
        db_admin = signup_admin(admin, db)
        return db_admin
    except Exception as e:
        raise e
    
def login_admin_controller(email: str, password: str, db: Session) :  
    try : 
        token = login_admin(email, password, db) 
        return token
    except Exception as e : 
        raise e

## ************************************* MODERATOR **********************************

def signup_moderator_controller(mod: ModeratorModel, db: Session):
    try:
        db_mod = signup_moderator(mod, db)
        return db_mod
    except Exception as e:
        raise e
    
def login_moderator_controller(email: str, password: str, db: Session) :  
    try : 
        token = login_moderator(email, password, db) 
        return token
    except Exception as e : 
        raise e
