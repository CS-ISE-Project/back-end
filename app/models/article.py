from typing import Optional

from pydantic import BaseModel

# ! URL type should be changed to a resp

class ArticleModel(BaseModel):
    id: Optional[int]
    title: str
    summury : str
    url: str
    text : str
    institues: str
    authors : str
    references: str
    id_favorites : Optional[int]