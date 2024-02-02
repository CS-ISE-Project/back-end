import os
import shutil

from app.config.config import UPLOAD_DIR

def save_local_pdf(file, key):
    filename = f"{key}.pdf"
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
        
def save_gdrive_pdf(file, key):
    filename = f"{key}.pdf"
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, 'wb') as f:
        f.write(file)
        
def delete_pdf(key):
    filename = f"{key}.pdf"
    file_path = os.path.join(UPLOAD_DIR, filename)
    os.remove(file_path)
        
def path_from_key(key):
    return f"{UPLOAD_DIR}/{key}.pdf"

def gdrive_download_link(link):
    file_id = link.split("/")[-2]
    return f"https://drive.google.com/uc?id={file_id}"