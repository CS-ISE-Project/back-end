from fastapi import APIRouter, Depends

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.utils.jwt import verify_token

from typing import List
from app.models.query import AdvanceQueryModel
from app.models.article import ArticleModel
from app.controllers.search_controller import simple_search_controller, advanced_search_controller

auth_scheme=HTTPBearer()
router = APIRouter()

@router.post("/simple", response_model=List[ArticleModel]) 
def simple_search(query: str, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, 'user')
    return simple_search_controller(query)

@router.post("/advanced", response_model=List[ArticleModel])
def advanced_search(query: AdvanceQueryModel, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, 'user')
    return advanced_search_controller(query)
