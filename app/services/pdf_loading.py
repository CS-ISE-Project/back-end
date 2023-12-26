import os
import time
import json
from app.utils.time import format_time

from unstructured.documents.elements import NarrativeText, PageBreak, Title, ListItem, EmailAddress
from app.config.config import MIN_CATEGORIZED_ELEMENT_LENGTH, MIN_UNCATEGORIZED_ELEMENT_LENGTH, STRATEGY

from unstructured.partition.pdf import partition_pdf
from unstructured.staging.base import elements_to_json

dir_path = 'data'
articles_dir_path = os.path.join(dir_path, 'articles')
elements_dir_path = os.path.join(dir_path, 'elements')

uncategorized_text = 'UncategorizedText'
extracted_categories = ["Title", "NarrativeText", "PageBreak", "ListItem", "EmailAddress"]

processing_time = {}

for file_name in os.listdir(articles_dir_path):
    if os.path.isfile(os.path.join(articles_dir_path, file_name)) and file_name.endswith(".pdf"):
        pdf_path = os.path.join(articles_dir_path, file_name)
        article_name = file_name.split(".")[0]
        
        print("[Processing] " + article_name)
        s = time.time()
        elements = partition_pdf(
            pdf_path,
            strategy=STRATEGY,
            include_page_breaks=True,
            include_metadata=False,
            unique_element_ids=True,
            languages=["eng"],
            )
        e = time.time()
        format_time("Partitioning", s, e)
        processing_time[article_name] = f"{e - s:.2f}"

        os.makedirs(os.path.join(elements_dir_path, STRATEGY), exist_ok=True)
        json_path = os.path.join(elements_dir_path, STRATEGY, article_name+".json")
        
        # saved_elements = [el for el in elements if ((el.category in extracted_categories and len(el.text) >= MIN_CATEGORIZED_ELEMENT_LENGTH) or (el.category == uncategorized_text and len(el.text) >= MIN_UNCATEGORIZED_ELEMENT_LENGTH))]
        
        elements_to_json(elements, json_path)
        print("[Saved] " + json_path)
        print("\n")
        
with open(os.path.join('app', 'logs', 'article_loading.json'), 'w') as f:
    json.dump(processing_time, f, indent=4)        