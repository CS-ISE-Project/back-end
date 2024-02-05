from app.utils.text import get_date

from app.models.article import ArticleModel, CompleteArticleModel
from app.schemas.article import Article

def model_to_db(article: ArticleModel):
    return Article(
        url = article.url,
        publication_date = get_date(article.publication_date),
        title = article.title,
        authors = str(article.authors),
        institutes = str(article.institutes),
        keywords = str(article.keywords),
        abstract = article.abstract,
        content = article.content,
        references = str(article.references)
    )
    
def db_to_model(article: Article, include_id: bool = True):
    if include_id:
        return CompleteArticleModel(
            id = article.id,
            url = article.url,
            publication_date = str(article.publication_date),
            title = article.title,
            authors = eval(article.authors),
            institutes = eval(article.institutes),
            keywords = eval(article.keywords),
            abstract = article.abstract,
            content = article.content,
            references = eval(article.references)
        )
    else:
        return ArticleModel(
            url = article.url,
            publication_date = str(article.publication_date),
            title = article.title,
            authors = eval(article.authors),
            institutes = eval(article.institutes),
            keywords = eval(article.keywords),
            abstract = article.abstract,
            content = article.content,
            references = eval(article.references)
        )

def es_to_model(hit):
    return CompleteArticleModel(
        id = hit['_id'],
        url = hit['_source']['url'],
        publication_date = str(hit['_source']['publication_date']),
        title = hit['_source']['title'],
        authors = hit['_source']['authors'],
        institutes = hit['_source']['institutes'],
        keywords = hit['_source']['keywords'],
        abstract = hit['_source']['abstract'],
        content = hit['_source']['content'],
        references = hit['_source']['references']
    )
