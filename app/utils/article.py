from app.models.article import ArticleModel
from app.schemas.article import Article

def model_to_db(article: ArticleModel):
    return Article(
        title = article.title,
        url = article.url,
        authors = str(article.authors),
        institutes = str(article.institutes),
        keywords = str(article.keywords),
        abstract = article.abstract,
        content = article.content,
        references = str(article.references)
    )
    
def db_to_model(article: Article):
    return ArticleModel(
        title = article.title,
        url = article.url,
        authors = eval(article.authors),
        institutes = eval(article.institutes),
        keywords = eval(article.keywords),
        abstract = article.abstract,
        content = article.content,
        references = eval(article.references)
    )