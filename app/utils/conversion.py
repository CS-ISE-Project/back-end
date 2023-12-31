import json

from pydantic import BaseModel

def jsonify(model: BaseModel, output_path: str):
    with open(output_path, "w") as f:
        json.dump(model.model_dump(), f, indent=4)