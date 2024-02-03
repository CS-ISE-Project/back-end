from sqlalchemy.orm import Session

from app.services.moderation_service import update_moderator_activation

def update_moderator_activation_controller(mod_id: int, is_active: bool, db: Session):
    try: 
        db_mod = update_moderator_activation(mod_id, is_active, db)
        return db_mod
    except Exception as e:
        raise e
