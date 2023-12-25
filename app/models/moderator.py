from typing import Optional

from pydantic import BaseModel

# ! email type should be changed

class ModeratorModel(BaseModel):
    id: Optional[int]
    first_name: str
    last_name : str
    email: str
    password : str
    isActive : bool
    