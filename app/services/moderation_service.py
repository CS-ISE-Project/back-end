from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from app.services.moderator_service import update_moderator_state

def update_moderator_activation(mod_id: int, is_active: bool, db: Session):
    try:
        updated_moderator = update_moderator_state(mod_id, is_active, db)
        return updated_moderator
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while updating the moderator state. Error: {str(e)}"
        )
