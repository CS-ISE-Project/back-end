from sqlalchemy.orm import Session

from app.models.admin import AdminModel, UpdateAdminModel, CompleteAdminModel

from app.services.admin_service import get_admin, create_admin, update_admin, delete_admin, get_all_admins

def get_all_admins_controller(db : Session):
    try:
        db_admin = get_all_admins(db)
        return db_admin
    except Exception as e:
        raise e

def get_admin_controller(admin_id: int , db : Session):
    try:
        db_admin = get_admin(admin_id, db)
        return db_admin
    except Exception as e:
        raise e
     
def create_admin_controller(admin: AdminModel , db : Session) :
    try : 
        db_admin = create_admin(admin , db)
        return db_admin
    except Exception as e : 
        raise e
    
def update_admin_controller(admin_id : int , updated_admin: UpdateAdminModel , db : Session) : 
    try : 
        db_admin = update_admin(admin_id, updated_admin , db)
        return db_admin
    except Exception as e : 
        raise e
    
def delete_admin_controller(admin_id : int , db : Session) : 
    try : 
        db_admin = delete_admin(admin_id,db)
        return db_admin
    except Exception as e : 
        raise e
