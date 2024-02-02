from app.services.upload_service import upload_local_file, upload_gdrive_file

def upload_local_file_controller(file):
    try:
        return upload_local_file(file)
    except Exception as e:
        raise e

def upload_gdrive_file_controller(link):
    try:
        return upload_gdrive_file(link)
    except Exception as e:
        raise e
