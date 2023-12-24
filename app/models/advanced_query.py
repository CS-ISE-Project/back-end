from pydantic import BaseModel
from typing import Optional
class AdvanceQueryModel(BaseModel):
    title : Optional[str]
    headline : Optional[str] # Keywords !! to be changed
    content : Optional[str]
    authors : Optional[str]
    institutes : Optional[str]