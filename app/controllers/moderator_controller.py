from sqlalchemy.orm import Session

from app.models.moderator import ModeratorModel

from app.services.moderator_service import create_moderator, get_moderator, get_all_moderators, update_moderator, delete_moderator 

def get_all_moderator_controller(db: Session):
    try:
        db_mod = get_all_moderators(db)
        return db_mod
    except Exception as e:
        raise e
    
def get_moderator_controller(mod_id: int, db: Session):
    try:
        db_mod = get_moderator(mod_id, db)
        return db_mod
    except Exception as e:
        raise e
      
def create_moderator_controller(mod: ModeratorModel, db: Session) :
    try : 
        db_mod = create_moderator(mod , db)
        return db_mod
    except Exception as e : 
        raise e
     
def update_moderator_controller(mod_id: int, updated_mod: ModeratorModel, db: Session) : 
    try : 
        db_mod = update_moderator(mod_id, updated_mod , db)
        return db_mod
    except Exception as e : 
        raise e
      
def delete_moderator_controller(mod_id: int, db: Session) : 
    try : 
        db_mod = delete_moderator(mod_id,db)
        return db_mod
    except Exception as e : 
        raise e
