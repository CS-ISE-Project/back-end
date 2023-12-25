from pydantic import BaseModel

class ModeratorModel(BaseModel):
    id: int | None
    first_name: str
    last_name : str
    email: str
    password : str
    is_active : bool
    