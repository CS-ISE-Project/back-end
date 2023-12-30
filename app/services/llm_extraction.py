import os
import time
import json

from app.utils.time import format_time
from app.utils.llm import cost

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from app.config.creds import OPENAI_API_KEY
from app.config.config import MODEL_NAME, MODEL_TEMPERATURE

llm = ChatOpenAI(model_name=MODEL_NAME, temperature=MODEL_TEMPERATURE, openai_api_key=OPENAI_API_KEY)

prompt= PromptTemplate(
    input_variables=['article_page'],
    template="""
    ROLE: You are specialized in extracting information from Articles.
    TASK: Given a parsed article page, your mission is to accurately and authentically extract the required information from the article.
    GUIDELINES:
    - If an information is not present in the article, just set it as an empty string.
    - If an information is present but not requested, just ignore it.
    - As parsing might not be completely accurate, a reasoning about the coherent information is also required.
    SECTIONS NEEDED:
    - Artcile Title
    - Article Authors
    - Article Institutes: The institutes of the authors
    - Article Keywords
    - Article Abstract
    - Article Permissions
    - Article Content: Mainly it will be a part of the article introduction which will be then joined with the rest of the article in further processing.
    OUTPUT FORMAT: The output should be a JSON object with the following structure:
    {{
        "title": str,
        "authors": list[str],
        "institutes": list[str],
        "keywords": list[str],
        "abstract": str,
        "permissions": str,
        "content": str,    
    }}
    INPUT: The following is the parsed article page:
    {article_page}
    
    OUTPUT JSON:
    """
)

chain = LLMChain(llm=llm, prompt=prompt)

def extract_article_information(article_page: str) -> dict:
    return eval(chain.run(article_page=article_page))

if __name__ == '__main__':
    logs = {}
    for filname in os.listdir('app/data/content'):
        with open(f'app/data/content/{filname}', 'r') as f:
            article_page = json.load(f)[0]
            
        print(f'Extracting information from {filname}')
        s = time.time()
        info = extract_article_information(article_page)
        e = time.time()
        format_time('Extraction Time', s, e)
        
        extraction_cost = cost(prompt.format(article_page=article_page), str(info))
        print(f'Cost: {extraction_cost}')
        
        with open(f'app/data/infos/{filname}', 'w') as f:
            json.dump(info, f, indent=4)
            
        logs[filname] = {
            'extraction_time': f"{e-s:.2f}",
            'extraction_cost': extraction_cost
        }
        
    with open('app/logs/extraction.json', 'w') as f:
        json.dump(logs, f, indent=4)