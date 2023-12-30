import os
import re
import json
import time

from app.utils.time import format_time

def extract_content_and_references(article_content): 
    references_pattern = re.compile(r'\bREFERENCES\b')
    reference_pattern = re.compile(r'\[\d+\]\s+.*?(?=\[\d+\]|\Z)', re.DOTALL)
    
    references = []
    
    found_references = False
    
    for page in article_content:
        if not found_references:
            match = re.search(references_pattern, page)
            if match:
                found_references = True
                
                refs = page[match.end():]
                matches = reference_pattern.findall(refs)
                for ref_match in matches:
                    references.append(ref_match)
        else:
            refs = page
            matches = reference_pattern.findall(refs)
            for ref_match in matches:
                references.append(ref_match)
                
    return references

if __name__ == '__main__':
    for filname in os.listdir('app/data/content'):
        with open(f'app/data/content/{filname}', 'r') as f:
            article_content = json.load(f)[1:]
                
        print(f'Extracting content and references from {filname}')
        s = time.time()
        references = extract_content_and_references(article_content)
        e = time.time()
        format_time('Extraction Time', s, e)
        
        with open(f'app/data/refs/{filname}', 'w') as f:
            json.dump(references, f, indent=4)