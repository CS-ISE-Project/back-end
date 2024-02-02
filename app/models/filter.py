from typing import List,Tuple
from pydantic import BaseModel

class FilterModel(BaseModel):
    authors : List[str] = []
    institues: List[str] = []
    keywords: List[str] =[]
    date_interval : Tuple[str,str] = ('','')