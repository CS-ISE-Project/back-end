import os
import time
import json

from app.utils.conversion import jsonify
from app.utils.time import format_time

from app.services.article_loading_service import load_article

if __name__ == "__main__":
    save_articles = True
    
    times = {}
    pdf_dir = "app/data/articles/"
    content_dir = "app/data/content/"
    
    for pdf in os.listdir(pdf_dir):
        pdf_path = os.path.join(pdf_dir, pdf)
        
        s = time.time()
        article = load_article(pdf_path)
        e = time.time()
        format_time(f'Loading {pdf}', s, e)
        times[pdf] = round(e-s, 2)
        
        if save_articles:
            jsonify(article, os.path.join(content_dir, pdf.replace(".pdf", ".json")))
        
    with open('app/logs/loading.json', 'w') as f:
        json.dump(times, f, indent=4)