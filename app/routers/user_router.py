from typing import List
from fastapi import APIRouter, Depends
from app.controllers.user_controller import get_all_users_controller, create_user_controller, get_user_controller , update_user_controller , delete_user_controller
from app.models.user import UserModel , CompleteUserModel
from app.scripts.database.setup import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=List[CompleteUserModel])
def read_all_users(db : Session = Depends(get_db)):
    return get_all_users_controller(db)

@router.get("/{user_id}", response_model=CompleteUserModel)
def read_user(user_id: int, db : Session = Depends(get_db)):
    return get_user_controller(user_id,db)

@router.post("/", response_model=UserModel)
def create_user(user: UserModel , db : Session = Depends(get_db)):
    return create_user_controller(user , db)

@router.put("/{user_id}", response_model=UserModel) 
def update_admin(user_id: int, updated_user : UserModel , db : Session = Depends(get_db) ) :
    return update_user_controller(user_id, updated_user, db)


# TODO : Refactor the code so there no response body (and use the 204 status code)
@router.delete("/{user_id}" , response_model=UserModel )
def delete_admin(user_id: int, db : Session = Depends(get_db)):
    return delete_user_controller(user_id,db)        