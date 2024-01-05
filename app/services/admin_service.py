from fastapi import Depends, HTTPException, Response , status

from sqlalchemy.orm import Session

from app.schemas.admin import Admin
from app.models.admin import AdminModel, CompleteAdminModel, UpdateAdminModel
from app.services.moderator_service import update_isActive


def get_all_admins(db : Session) :
    admins = db.query(Admin).all()
    if not admins : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No admins found"
        )
    return admins

def get_admin(admin_id: int , db : Session):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if admin is None : 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Admin with id {admin_id} not found"
        )
    return admin

def get_admin_by_email(admin_email: str , db: Session):
    return db.query(Admin).filter(Admin.email == admin_email).first()

def create_admin(admin: AdminModel , db: Session):
    try :
        db_admin = Admin(
            first_name=admin.first_name,
            last_name=admin.last_name,
            email = admin.email,
            password = admin.password)
    
        db.add(db_admin)
        db.commit()
        db.refresh(db_admin)
        return db_admin
    
    except Exception as e : 
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the admin. Error: {str(e)}"
        )

def update_admin(admin_id: int , updated_admin: UpdateAdminModel , db: Session): 
    db_admin = db.query(Admin).filter(Admin.id == admin_id).first()

    if db_admin is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Admin with id {db_admin} not found"
        )
     
    try:
        db_admin.first_name=updated_admin.first_name,
        db_admin.last_name=updated_admin.last_name,
        db_admin.email = updated_admin.email,
    
        db.commit()
        db.refresh(db_admin)
        return db_admin
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the admin. Error: {str(e)}"
        )
        
def delete_admin(admin_id: int , db: Session):
    db_admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if db_admin is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Admin with id {db_admin} not found"
        )
    
    try :
        db.delete(db_admin)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while creating the admin. Error: {str(e)}"
        )

def activate_moderator(mod_id : int , db : Session) : 
    try :
        activated_mod = update_isActive(mod_id , True , db)
        return activated_mod
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while activating the moderator. Error: {str(e)}"
        )