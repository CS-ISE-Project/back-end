from app.models.user import UserModel
from app.models.admin import AdminModel
from app.models.moderator import ModeratorModel
from sqlalchemy.orm import Session
from app.services.auth_service import signup_User , login_User , signup_Admin , login_Admin


## ************************************* USER **********************************


def signup_User_controller(user: UserModel , db : Session):
    try:
        db_user = signup_User(user, db)
        return db_user
    except Exception as e:
        raise e
    
def login_User_controller(email : str, password : str , db : Session) :  
    try : 
        token = login_User(email, password, db) 
        return token
    except Exception as e : 
        raise e
    


## ************************************* ADMIN **********************************
    
def signup_Admin_controller(admin: AdminModel , db : Session):
    try:
        db_admin = signup_Admin(admin, db)
        return db_admin
    except Exception as e:
        raise e
    
    
def login_Admin_controller(email : str, password : str , db : Session) :  
    try : 
        token = login_Admin(email, password, db) 
        return token
    except Exception as e : 
        raise e
    