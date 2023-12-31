from app.models.article import ArticlePDF
from app.utils.extraction import get_content_and_references, get_content_sections

from langchain.document_loaders import PyMuPDFLoader
from app.services.llm_extraction import extract_article_information

def load_article(path: str) -> ArticlePDF:
    loader = PyMuPDFLoader(path)
    data = loader.load()
        
    info = extract_article_information(data[0].page_content)
    content_dump = info['content'] + '\n'
    info.pop('content')
    
    later_content, references = get_content_and_references(data[1:])
    content_dump += later_content
    sections = get_content_sections(content_dump)
    
    return ArticlePDF(info=info, sections=sections, references=references)