from fastapi import APIRouter, Depends
from app.controllers.admin_controller import get_admin_controller
from app.models.admin import AdminModel
from app.scripts.database.setup import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/{admin_id}", response_model=AdminModel)
def read_admin(admin_id: int, db : Session = Depends(get_db)):
    return get_admin_controller(admin_id,db)