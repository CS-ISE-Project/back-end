from fastapi import Depends, HTTPException, Response , status

from sqlalchemy.orm import Session

from app.schemas.moderator import Moderator
from app.models.moderator import ModeratorModel, UpdateModeratorModel, CompleteModeratorModel , ActiveModeratorModel

def get_all_moderators(db: Session):
    mods = db.query(Moderator).all()
    if not mods:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No moderators found"
        )
    return mods

def get_moderator_by_email(mod_mail: str , db: Session) :
    return db.query(Moderator).filter(Moderator.email == mod_mail).first()

def get_moderator(mod_id: int , db : Session):
    mod =  db.query(Moderator).filter(Moderator.id == mod_id).first()
    if mod is None : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Moderator with id {mod_id} not found"
        )
    return mod

def create_moderator(mod: ModeratorModel , db: Session):
    try:
        db_mod = Moderator(
            first_name=mod.first_name,
            last_name=mod.last_name,
            email = mod.email,
            password = mod.password)
    
        db.add(db_mod)
        db.commit()
        db.refresh(db_mod)
        return db_mod
    
    except Exception as e: 
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the moderator. Error: {str(e)}"
        )        

def update_moderator(mod_id: int , updated_mod: UpdateModeratorModel, db: Session) : 
    db_mod = db.query(Moderator).filter(Moderator.id == mod_id).first()
    if db_mod is None : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Moderator with id {mod_id} not found"
        )    
    try :     
        db_mod.first_name=updated_mod.first_name,
        db_mod.last_name=updated_mod.last_name,
        db_mod.email = updated_mod.email,
    
        db.commit()
        db.refresh(db_mod)
        return db_mod
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while updating the user. Error: {str(e)}"
        )


def update_isActive (mod_id : int, activate : bool, db: Session) :
    db_mod = db.query(Moderator).filter(Moderator.id == mod_id).first()
    if db_mod is None : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Moderator with id {mod_id} not found"
        ) 
    try : 
        db_mod.is_active = activate
        
        db.commit()
        db.refresh(db_mod)
        return db_mod
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while updating the moderator. Error: {str(e)}"
        )


def delete_moderator(mod_id : int , db : Session) :
    db_mod = db.query(Moderator).filter(Moderator.id == mod_id).first()
    if db_mod is None : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Moderator with id {mod_id} not found"
        )  
        
    try:        
        db.delete(db_mod)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while deleting the moderator. Error: {str(e)}"
        )
