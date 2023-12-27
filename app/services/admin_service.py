from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.admin import Admin
from app.models.user import UserModel



def get_admin(admin_id: int , db : Session):
    return db.query(Admin).filter(Admin.id == admin_id).first()
