from app.utils.text import clean_text

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from app.config.creds import OPENAI_API_KEY
from app.config.config import MODEL_NAME, MODEL_TEMPERATURE

llm = ChatOpenAI(model_name=MODEL_NAME, temperature=MODEL_TEMPERATURE, openai_api_key=OPENAI_API_KEY)

prompt= PromptTemplate(
    input_variables=['article_page'],
    template="""ROLE: You are specialized in extracting information from Articles
TASK: Given a parsed article first page, your mission is to accurately and authentically extract the required information from the article
GUIDELINES:
- As parsing might not be completely accurate, resulting in mixing sections content, a reasoning about the coherent information is required.
SECTIONS NEEDED:
- Publication Date: Even if it it is not clear whether the date you will encounter is the publication date, it is the only date you will find in the article. If an interval is found, just set the first date as the publication date.
- Artcile Title
- Article Authors
- Article Institutes: The institutes of the authors
- Article Keywords
- Article Abstract
- Article Content: Sections that proceed the Abstract. Please preserve the title of any section you encounter with its indexing as it is crucial for further regex preprocessing, example: 1. Introduction, 2. Other section (That is only an example, authenticity is highly needed, so be careful on section indexing and naming) Add a new line after the title, and assemble all section content in one paragraph.
OUTPUT FORMAT: The output should be a JSON object with the following structure:
{{
    "publication_date": str (convert to DD-MM-YYYY format),
    "title": str,
    "authors": list[str],
    "institutes": list[str],
    "keywords": list[str],
    "abstract": str,
    "content": str,    
}}
INPUT: The following is the parsed article page:
{article_page}

OUTPUT JSON:
"""
)

chain = LLMChain(llm=llm, prompt=prompt)

def extract_article_information(article_page: str) -> dict:
    return eval(chain.run(article_page=clean_text(article_page)))
