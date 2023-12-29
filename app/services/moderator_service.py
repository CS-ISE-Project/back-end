from sqlalchemy.orm import Session
from app.schemas.moderator import Moderator
from app.models.moderator import ModeratorModel



def get_moderator(mod_id: int , db : Session):
    return db.query(Moderator).filter(Moderator.id == mod_id).first()

def create_moderator(mod: ModeratorModel , db: Session) :
    db_mod = Moderator(
        first_name=mod.first_name,
        last_name=mod.last_name,
        email = mod.email,
        password = mod.password)
    
    db.add(db_mod)
    db.commit()
    db.refresh(db_mod)
    return db_mod


# TODO : A better solution to do is to separate the password modification from the update endpoint
def update_moderator(mod_id : int , updated_mod : ModeratorModel , db: Session) : 
    db_mod = db.query(Moderator).filter(Moderator.id == mod_id).first()
    
    db_mod.first_name=updated_mod.first_name,
    db_mod.last_name=updated_mod.last_name,
    db_mod.email = updated_mod.email,
    db_mod.password = updated_mod.password
    
    db.commit()
    db.refresh(db_mod)
    return db_mod

def delete_admin(mod_id : int , db : Session) :
    db_mod = db.query(Moderator).filter(Moderator.id == mod_id).first()
    
    db.delete(db_mod)
    db.commit()
    return db_mod
        