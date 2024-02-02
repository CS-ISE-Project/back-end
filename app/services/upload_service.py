import requests

from fastapi import HTTPException, status

from app.models.upload import SuccessfulLocalUpload, SuccessfulGdriveUpload

from app.utils.randomness import unique_id
from app.utils.upload import save_local_pdf, save_gdrive_pdf, gdrive_download_link

def upload_local_file(file):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are allowed"
        )
    try:
        key = unique_id()
        save_local_pdf(file, key)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while uploading the file. Error: {str(e)}"
        )
    return SuccessfulLocalUpload(message="File uploaded successfully!", file_name=file.filename, file_key=key)

def upload_gdrive_file(link):
    try:
        download_link = gdrive_download_link(link)
        file = requests.get(download_link).content
        key = unique_id()
        save_gdrive_pdf(file, key)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while uploading the file. Error: {str(e)}"
        )
    return SuccessfulGdriveUpload(message="File uploaded successfully!", file_key=key)
