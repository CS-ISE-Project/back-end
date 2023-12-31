from pydantic import BaseModel , EmailStr
from typing import List , Dict
from app.models.article import ArticleModel


# ? To create users 
class UserModel(BaseModel):
    # ? Adding the id here will oblige us to precise an ID when creating the object
    #id: int | None
    first_name: str
    last_name : str
    email: EmailStr
    password : str


# ? for the complete response purpose : getting users
class CompleteUserModel(BaseModel) :
    id: int | None
    first_name: str
    last_name : str
    email: str
    password : str
    
    
# ? User and favorites Model : 
class UserAndFavoritesModel(BaseModel):
    user : CompleteUserModel
    favorites : Dict[int , ArticleModel]



# ? to update the users, we need the password to be treated at something else, and we must verify it again (as any decent website)
class UpdateUserModel(BaseModel) :
    #id: int | None
    first_name: str
    last_name : str
    email: str
    #password : str
    