from app.models.moderator import ModeratorModel
from sqlalchemy.orm import Session
from app.services.moderator_service import create_moderator, get_moderator , update_moderator , delete_admin
 
    
def get_moderator_controller(mod_id: int , db : Session):
    try:
        db_mod = get_moderator(mod_id, db)
        return db_mod
    except Exception as e:
        raise e
    
    
def create_moderator_controller(mod: ModeratorModel , db : Session) :
    try : 
        db_mod = create_moderator(mod , db)
        return db_mod
    except Exception as e : 
        raise e
    
    
def update_moderator_controller(mod_id : int , updated_mod: ModeratorModel , db : Session) : 
    try : 
        db_mod = update_moderator(mod_id, updated_mod , db)
        return db_mod
    except Exception as e : 
        raise e
    
    
def delete_moderator_controller(mod_id : int , db : Session) : 
    try : 
        db_mod = delete_admin(mod_id,db)
        return db_mod
    except Exception as e : 
        raise e
