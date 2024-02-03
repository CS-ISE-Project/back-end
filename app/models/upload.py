from pydantic import BaseModel

class SuccessfulLocalUpload(BaseModel):
    message: str
    file_name: str
    file_key: str

class SuccessfulGdriveUpload(BaseModel):
    message: str
    file_key: str
