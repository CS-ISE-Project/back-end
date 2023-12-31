from app.models.user import UserModel , UpdateUserModel
from sqlalchemy.orm import Session
from app.services.user_service import create_user, get_user , update_user , delete_user , get_all_users


def get_all_users_controller(db : Session):
    try:
        db_users = get_all_users(db)
        return db_users
    except Exception as e:
        raise e
     
    
def get_user_controller(user_id: int , db : Session):
    try:
        db_user = get_user(user_id, db)
        return db_user
    except Exception as e:
        raise e
    
    
def create_user_controller(user: UserModel , db : Session) :
    try : 
        db_user = create_user(user , db)
        return db_user
    except Exception as e : 
        raise e
    
    
def update_user_controller(user_id : int , updated_user: UpdateUserModel , db : Session) : 
    try : 
        db_user = update_user(user_id, updated_user , db)
        return db_user
    except Exception as e : 
        raise e
    
    
def delete_user_controller(user_id : int , db : Session) : 
    try : 
        db_user = delete_user(user_id,db)
        return db_user
    except Exception as e : 
        raise e


