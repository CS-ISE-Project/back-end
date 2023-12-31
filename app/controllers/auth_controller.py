from app.models.user import UserModel
from sqlalchemy.orm import Session
from app.services.auth_service import signup , login

def signup_controller(user: UserModel , db : Session):
    try:
        db_user = signup(user, db)
        return db_user
    except Exception as e:
        raise e
    
def login_controller(email : str, password : str , db : Session) :  
    try : 
        token = login(email, password, db) 
        return token
    except Exception as e : 
        raise e