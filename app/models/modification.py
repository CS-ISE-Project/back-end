from pydantic import BaseModel

class ModificationModel(BaseModel):
    id_moderator: int
    id_article : int
    date: str
    time: str
