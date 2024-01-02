from pydantic import BaseModel, EmailStr

class AdminModel(BaseModel):
    # ? Adding the id here will oblige us to precise an ID when creating the object
    #id: int | None
    first_name: str
    last_name : str
    email: EmailStr
    password : str




# ? for the complete response purpose : getting users
class CompleteAdminModel(BaseModel) :
    id: int | None
    first_name: str
    last_name : str
    email: str
    #password : str
    


# ? to update the users, we need the password to be treated at something else, and we must verify it again (as any decent website)
class UpdateAdminModel(BaseModel) :
    #id: int | None
    first_name: str
    last_name : str
    email: str
    #password : str