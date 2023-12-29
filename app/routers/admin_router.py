from fastapi import APIRouter, Depends
from app.controllers.admin_controller import get_admin_controller , create_admin_controller , update_admin_controller , delete_admin_controller
from app.models.admin import AdminModel
from app.scripts.database.setup import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{admin_id}", response_model=AdminModel)
def read_admin(admin_id: int, db : Session = Depends(get_db)):
    return get_admin_controller(admin_id,db)

@router.post("/", response_model=AdminModel) 
def create_admin(admin: AdminModel , db : Session = Depends(get_db)) :
    return create_admin_controller(admin, db)

@router.put("/{admin_id}", response_model=AdminModel) 
def update_admin(admin_id: int, updated_admin : AdminModel , db : Session = Depends(get_db) ) :
    return update_admin_controller(admin_id, updated_admin, db)


# TODO : Refactor the code so there no response body (and use the 204 status code)
@router.delete("/{admin_id}" , response_model=AdminModel )
def delete_admin(admin_id: int, db : Session = Depends(get_db)):
    return delete_admin_controller(admin_id,db)        