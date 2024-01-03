from typing import List, Dict, Union

from pydantic import BaseModel

class ArticleModel(BaseModel):
    url: str
    title: str
    authors : List[str]
    institues: List[str]
    keywords: List[str]
    abstract : str
    content : str
    references: List[str]
    
class ArticlePDF(BaseModel):
    info: Dict[str, Union[str, List[str]]]
    content: str
    references: List[str]