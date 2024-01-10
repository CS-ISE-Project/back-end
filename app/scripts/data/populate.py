import os
import time
import json

from app.scripts.database.setup import get_db_session

from app.utils.time import format_time
from app.utils.conversion import modelize_article

from app.controllers.article_controller import create_article_controller

if __name__ == "__main__":
    times = {}
    articles_dir = "app/data/content/"
    
    for article_path in os.listdir(articles_dir):
        article = modelize_article(os.path.join(articles_dir, article_path))
        
        s = time.time()
        db = get_db_session()
        create_article_controller(article, db=db)
        e = time.time()
        format_time(f'Creating Article {article_path}', s, e)
        
        times[article_path] = round(e-s, 2)
    
    with open('app/logs/population.json', 'w') as f:
        json.dump(times, f, indent=4)
