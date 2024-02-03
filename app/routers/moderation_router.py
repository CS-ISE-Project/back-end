from fastapi import APIRouter, Depends

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.utils.jwt import verify_token

from sqlalchemy.orm import Session
from app.scripts.database.setup import get_db

from app.models.moderator import CompleteModeratorModel, ModeratorStateModel
from app.controllers.moderation_controller import update_moderator_activation_controller

auth_scheme = HTTPBearer()
router = APIRouter()

@router.put("/activation", response_model=CompleteModeratorModel)
def update_moderator_activation(moderator_state: ModeratorStateModel, db: Session = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials , 'admin')
    return update_moderator_activation_controller(moderator_state.id, moderator_state.is_active, db)
