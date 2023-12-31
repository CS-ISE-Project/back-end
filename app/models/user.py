from pydantic import BaseModel , EmailStr

class UserModel(BaseModel):
    # ? Adding the id here will oblige us to precise an ID when creating the object
    #id: int | None
    first_name: str
    last_name : str
    email: EmailStr
    password : str
    
    
class CompleteUserModel(BaseModel) :
    id: int | None
    first_name: str
    last_name : str
    email: str
    password : str
    

class UpdateUserModel(BaseModel) :
    #id: int | None
    first_name: str
    last_name : str
    email: str
    #password : str
    