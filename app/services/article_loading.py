import os
import json

from langchain.document_loaders import UnstructuredPDFLoader, PyPDFLoader, PyMuPDFLoader, AmazonTextractPDFLoader

modes = ["paged", "elements"]

articles_path = "data/articles"
content_path = "data/content"

for mode in modes:
    os.makedirs(os.path.join(content_path, mode), exist_ok=True)

for file_name in os.listdir(articles_path):
    if os.path.isfile(os.path.join(articles_path, file_name)) and file_name.endswith(".pdf"):
        article_path = os.path.join(articles_path, file_name)
        
        print("[Processing] " + file_name)
        
        # for mode in modes:
        print("[Mode] " + mode)
        
        # loader = UnstructuredPDFLoader(article_path, mode=mode)
        # loader = PyPDFLoader(article_path)
        loader = PyMuPDFLoader(article_path)
        # loader = AmazonTextractPDFLoader(article_path)
        
        data = loader.load()
        
        elements = []
        for document in data:
            elements.append(document.page_content)
        
        with open(os.path.join(content_path, 'pymupdf', file_name.split(".")[0]+".json"), "w") as f:
            json.dump(elements, f, indent=4)