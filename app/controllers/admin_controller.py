
from app.models.admin import AdminModel
from sqlalchemy.orm import Session
from app.services.admin_service import get_admin



def get_admin_controller(admin_id: int , db : Session):
    try:
        db_admin = get_admin(admin_id, db)
        return db_admin
    except Exception as e:
        raise e