import os

from app.models.article import ArticlePDF
from app.utils.pdf import articlePDF_to_json
from app.utils.text import clean_text

from langchain.document_loaders import PyMuPDFLoader

def load_article(path: str) -> ArticlePDF:
    loader = PyMuPDFLoader(path)
    data = loader.load()
    pages = []
    for document in data:
        pages.append(clean_text(document.page_content))
    return ArticlePDF(pages=pages)

if __name__ == "__main__":
    pdf_dir = "app/data/articles/"
    content_dir = "app/data/content/"
    
    for pdf in os.listdir(pdf_dir):
        pdf_path = os.path.join(pdf_dir, pdf)
        article = load_article(pdf_path)
        articlePDF_to_json(article, os.path.join(content_dir, pdf.replace(".pdf", ".json")))