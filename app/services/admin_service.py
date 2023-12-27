from sqlalchemy.orm import Session
from app.schemas.admin import Admin
from app.models.admin import AdminModel



def get_admin(admin_id: int , db : Session):
    return db.query(Admin).filter(Admin.id == admin_id).first()

def create_admin(admin: AdminModel , db: Session) :
    db_admin = Admin(
        first_name=admin.first_name,
        last_name=admin.last_name,
        email = admin.email,
        password = admin.password)
    
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


# TODO : A better solution to do is to separate the password modification from the update endpoint
def update_admin(admin_id : int , updated_admin : AdminModel , db: Session) : 
    db_admin = db.query(Admin).filter(Admin.id == admin_id).first()
    
    db_admin.first_name=updated_admin.first_name,
    db_admin.last_name=updated_admin.last_name,
    db_admin.email = updated_admin.email,
    db_admin.password = updated_admin.password
    
    db.commit()
    db.refresh(db_admin)
    return db_admin

def delete_admin(admin_id : int , db : Session) :
    db_admin = db.query(Admin).filter(Admin.id == admin_id).first()
    
    db.delete(db_admin)
    db.commit()
    return db_admin
        
    
    
    

