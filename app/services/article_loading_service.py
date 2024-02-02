from fastapi import HTTPException, status

from app.models.article import ArticleModel
from app.utils.text import clean_content, is_date
from app.utils.extraction import get_content_and_references

from langchain.document_loaders import PyMuPDFLoader
from app.services.llm_extraction import extract_article_information

def load_article(path: str) -> ArticleModel:
    try:
        loader = PyMuPDFLoader(path)
        data = loader.load()
            
        info = extract_article_information(data[0].page_content)
        content = info['content'] + '\n'
        info.pop('content')
        
        later_content, references = get_content_and_references(data[1:])
        content += later_content
        content = clean_content(content)
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while loading the article. Error: {str(e)}"
        )
    
    return ArticleModel(
        url = '',
        publication_date = info['publication_date'] if is_date(info['publication_date']) else '',
        title = info['title'],
        authors = info['authors'],
        institutes = info['institutes'],
        keywords = info['keywords'],
        abstract = info['abstract'],
        content = content,
        references = references
    )
