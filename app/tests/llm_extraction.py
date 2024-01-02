import os
import time
import json

from app.utils.time import format_time
from app.utils.llm import cost

from langchain.document_loaders import PyMuPDFLoader
from app.services.llm_extraction import prompt, extract_article_information

if __name__ == '__main__':
    save_infos = False
    logs = {}
    
    for filname in os.listdir('app/data/articles'):
        loader = PyMuPDFLoader(f'app/data/articles/{filname}')
        article_page = loader.load()[0].page_content
            
        print(f'Extracting information from {filname}')
        s = time.time()
        info = extract_article_information(article_page)
        e = time.time()
        format_time('Extraction Time', s, e)
        
        extraction_cost = cost(prompt.format(article_page=article_page), str(info))
        print(f'Cost: {extraction_cost}')
        
        if save_infos:
            with open(f'app/data/infos/{filname}', 'w') as f:
                json.dump(info, f, indent=4)
            
        logs[filname] = {
            'extraction_time': round(e-s, 2),
            'extraction_cost': round(extraction_cost, 4)
        }
        
    with open('app/logs/extraction.json', 'w') as f:
        json.dump(logs, f, indent=4)