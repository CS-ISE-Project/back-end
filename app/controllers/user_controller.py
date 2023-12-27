from app.models.user import UserModel
from sqlalchemy.orm import Session
from app.services.user_service import create_user, get_user

def create_user_controller(user: UserModel):
    try:
        db_user = create_user(user)
        return db_user
    except Exception as e:
        raise e
 
 
    
def get_user_controller(user_id: int , db : Session):
    try:
        db_user = get_user(user_id, db)
        return db_user
    except Exception as e:
        raise e
    


