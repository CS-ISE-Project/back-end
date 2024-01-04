from pydantic import BaseModel
from typing import List

class AdvanceSearchModel(BaseModel):
    restricted : bool
    title : str
    keywords: List[str]
    authors : List[str]
    content : str