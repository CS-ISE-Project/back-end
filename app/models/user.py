from typing import Optional

from pydantic import BaseModel

# ! email type should be changed

class UserModel(BaseModel):
    id: Optional[int]
    first_name: str
    last_name : str
    email: str
    password : str
    id_favoris : Optional[int]