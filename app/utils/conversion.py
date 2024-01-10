import json

from pydantic import BaseModel
from app.models.article import ArticleModel

def jsonify(model: BaseModel, output_path: str):
    with open(output_path, "w") as f:
        json.dump(model.model_dump(), f, indent=4)
        
def modelize_article(input_path: str) -> ArticleModel:
    with open(input_path, "r") as f:
        data = json.load(f)
    return ArticleModel(**data)
