from app.models.article import ArticleModel
from app.utils.text import clean_content
from app.utils.extraction import get_content_and_references

from langchain.document_loaders import PyMuPDFLoader
from app.services.llm_extraction import extract_article_information

def load_article(path: str) -> ArticleModel:
    loader = PyMuPDFLoader(path)
    data = loader.load()
        
    info = extract_article_information(data[0].page_content)
    content = info['content'] + '\n'
    info.pop('content')
    
    later_content, references = get_content_and_references(data[1:])
    content += later_content
    content = clean_content(content)
    
    return ArticleModel(
        url = 'dummy',
        title = info['title'],
        authors = info['authors'],
        institutes = info['institutes'],
        keywords = info['keywords'],
        abstract = info['abstract'],
        content = content,
        references = references
    )