from pydantic import BaseModel

class AdminModel(BaseModel):
    id: int | None
    first_name: str
    last_name : str
    email: str
    password : str
