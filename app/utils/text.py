import re

def clean_text(text):
    cleaned_text = re.sub(r'[^\w\s.,:;/?!\'"-+=()[\]{}*%$@]', '', text)
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text

def get_reference_index(reference):
    match = re.match(r'\[(\d+)\]', reference)
    if match:
        return int(match.group(1))
    return None