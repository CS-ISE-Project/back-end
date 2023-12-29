from fastapi import APIRouter, Depends
from app.controllers.moderator_controller import create_moderator_controller, get_moderator_controller , update_moderator_controller , delete_moderator_controller
from app.models.moderator import ModeratorModel
from app.scripts.database.setup import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{mod_id}", response_model=ModeratorModel)
def read_moderator(mod_id: int, db : Session = Depends(get_db)):
    return get_moderator_controller(mod_id,db)

@router.post("/", response_model=ModeratorModel)
def create_moderator(mod: ModeratorModel , db : Session = Depends(get_db)):
    return create_moderator_controller(mod , db)

@router.put("/{mod_id}", response_model=ModeratorModel) 
def update_admin(mod_id: int, updated_mod : ModeratorModel , db : Session = Depends(get_db) ) :
    return update_moderator_controller(mod_id, updated_mod, db)


# TODO : Refactor the code so there no response body (and use the 204 status code)
@router.delete("/{mod_id}" , response_model=ModeratorModel )
def delete_admin(mod_id: int, db : Session = Depends(get_db)):
    return delete_moderator_controller(mod_id,db)        