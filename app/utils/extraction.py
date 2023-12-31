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
    
def detect_section_titles(text):
    pattern = r'((?:\d+\.)+\d*\s[A-Z][^\n\.]+)'
    matches = re.finditer(pattern, text)
    
    last_section = None
    true_matches = []
    
    for match in matches:
        indices = match.group(1).split()[0].split('.')
        if last_section == None and int(indices[0]) == 1:
            true_matches.append(match)
            last_section = indices
        elif last_section != None and (int(indices[0]) == int(last_section[0]) + 1 or int(indices[0]) == int(last_section[0])):
            true_matches.append(match)
            last_section = indices
            
    return true_matches 

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

def get_content_sections(content_dump):
    sections = {}
    section_matches = detect_section_titles(content_dump)
    for i in range(len(section_matches)):
        if i == len(section_matches) - 1:
            sections[clean_text(section_matches[i].group(1))] = clean_text(content_dump[section_matches[i].end():])
        else:
            sections[clean_text(section_matches[i].group(1))] = clean_text(content_dump[section_matches[i].end():section_matches[i+1].start()])
            
    return sections
    