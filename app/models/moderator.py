from pydantic import BaseModel , EmailStr

class ModeratorModel(BaseModel):
    first_name: str
    last_name : str
    email: EmailStr
    password : str    
    
class CompleteModeratorModel(BaseModel):
    id: int
    first_name: str
    last_name : str
    email: str
    is_active : bool

class UpdateModeratorModel(BaseModel):
    first_name: str
    last_name : str
    email: str

class ActiveModeratorModel(BaseModel):
    is_active : bool