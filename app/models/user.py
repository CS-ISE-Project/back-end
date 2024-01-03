from pydantic import BaseModel , EmailStr
from typing import Dict
from app.models.article import ArticleModel

class UserModel(BaseModel):
    first_name: str
    last_name : str
    email: EmailStr
    password : str

class CompleteUserModel(BaseModel):
    id: int
    first_name: str
    last_name : str
    email: str    
    
class UserFavoritesModel(BaseModel):
    user : CompleteUserModel
    favorites : Dict[int , ArticleModel]

class UpdateUserModel(BaseModel):
    first_name: str
    last_name : str
    email: str