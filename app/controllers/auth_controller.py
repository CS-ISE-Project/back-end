from app.models.user import UserModel
from sqlalchemy.orm import Session
from app.services.auth_service import signup

def signup_controller(user: UserModel , db : Session):
    try:
        db_user = signup(user, db)
        return db_user
    except Exception as e:
        raise e
    