from pydantic import BaseModel, EmailStr

class AdminModel(BaseModel):
    first_name: str
    last_name : str
    email: EmailStr
    password : str

class CompleteAdminModel(BaseModel) :
    id: int
    first_name: str
    last_name : str
    email: str

class UpdateAdminModel(BaseModel) :
    first_name: str
    last_name : str
    email: str