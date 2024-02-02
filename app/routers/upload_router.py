from fastapi import APIRouter, Depends, File, UploadFile

from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.utils.jwt import verify_token

from app.models.upload import SuccessfulLocalUpload, SuccessfulGdriveUpload
from app.controllers.upload_controller import upload_local_file_controller, upload_gdrive_file_controller

auth_scheme=HTTPBearer()
router = APIRouter()

@router.post("/local", response_model=SuccessfulLocalUpload)
def upload_local_file(file: UploadFile = File(...), token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, 'admin')
    return upload_local_file_controller(file)

@router.post("/gdrive", response_model=SuccessfulGdriveUpload)
def upload_gdrive_file(link: str, token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    verify_token(token.credentials, 'admin')
    return upload_gdrive_file_controller(link)
