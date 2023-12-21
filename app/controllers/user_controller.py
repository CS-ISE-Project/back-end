from app.models.user import UserModel

from app.services.user_service import create_user, get_user

def create_user_controller(user: UserModel):
    try:
        db_user = create_user(user)
        return db_user
    except Exception as e:
        raise e
    
def get_user_controller(user_id: int):
    try:
        db_user = get_user(user_id)
        return db_user
    except Exception as e:
        raise e