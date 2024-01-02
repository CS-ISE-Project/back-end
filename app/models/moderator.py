from pydantic import BaseModel , EmailStr
from typing import List , Dict

# ? For Creation
class ModeratorModel(BaseModel):
    #id: int | None
    first_name: str
    last_name : str
    email: EmailStr
    password : str
    #? to not let the update altern this field, and create a special endpoint to interact with it
    #is_active : bool
    
    

# ? for the complete response purpose : getting users
class CompleteModeratorModel(BaseModel):
    id: int | None
    first_name: str
    last_name : str
    email: str
    #password : str
    #? to not let the update altern this field, and create a special endpoint to interact with it
    #is_active : bool


# ? for the complete response purpose : getting users
class UpdateModeratorModel(BaseModel):
    #id: int | None
    first_name: str
    last_name : str
    email: str
    #password : str
    #? to not let the update altern this field, and create a special endpoint to interact with it
    #is_active : bool  

# ? the model for the admin to activate it 
class ActiveModeratorModel(BaseModel):
    is_active : bool
    
    
    
    