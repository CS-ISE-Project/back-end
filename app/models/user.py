from typing import Optional

from pydantic import BaseModel

class UserModel(BaseModel):
    id: Optional[int]
    username: str
    email: str