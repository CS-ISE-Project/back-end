from pydantic import BaseModel

class AdvanceQueryModel(BaseModel):
    restricted : bool | None
    title : str | None
    keywords : str | None
    content : str | None
    authors : str | None
    institutes : str | None