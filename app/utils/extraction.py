import re

from app.utils.text import clean_text

def get_reference_index(reference):
    match = re.match(r'\[(\d+)\]', reference)
    if match:
        return int(match.group(1))
    return None

def detect_references(text):
    pattern = r'\breferences\s*\[\d+\]\s*\w+'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.start()
    else:
        return None

def get_content_and_references(documents): 
    content = ''
    references = []
    found_references = False
    reference_pattern = re.compile(r'\[\d+\]\s+.*?(?=\[\d+\]|\Z)', re.DOTALL)  
    
    for document in documents:
        if found_references:
            refs = clean_text(document.page_content)
            matches = reference_pattern.findall(refs)
            for ref_match in matches:
                if get_reference_index(ref_match) == len(references) + 1:
                    references.append(ref_match)
        else:
            ref_start = detect_references(document.page_content)
            if not ref_start:
                content += document.page_content
            else:
                found_references = True
                refs = clean_text(document.page_content[ref_start:])
                content += document.page_content[:ref_start]
                matches = reference_pattern.findall(refs)
                for ref_match in matches:
                    if get_reference_index(ref_match) == len(references) + 1:
                        references.append(ref_match)
                        
    return content, references
