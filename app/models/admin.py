from typing import Optional

from pydantic import BaseModel

# ! email type should be changed to a resp

class AdminModel(BaseModel):
    id: Optional[int]
    first_name: str
    last_name : str
    email: str
    password : str
