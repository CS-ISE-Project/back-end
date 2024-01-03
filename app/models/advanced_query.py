from pydantic import BaseModel

class AdvanceQueryModel(BaseModel):
    restricted : bool
    title : str
    keywords : str
    content : str
    authors : str
    institutes : str