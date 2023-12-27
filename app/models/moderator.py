from pydantic import BaseModel

class ModeratorModel(BaseModel):
    #id: int | None
    first_name: str
    last_name : str
    email: str
    password : str
    #? to not let the update altern this field, and create a special edpoint to interact with it
    #is_active : bool
    