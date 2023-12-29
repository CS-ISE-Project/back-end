import json

from app.models.article import ArticlePDF

def articlePDF_to_json(article: ArticlePDF, output_path: str):
    with open(output_path, "w") as f:
        json.dump(article.pages, f, indent=4)