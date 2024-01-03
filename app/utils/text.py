import re

def clean_text(text: str):
    cleaned_text = re.sub(r'[^\w\s.,:;/?!\'"-+=()[\]{}*%$@]', '', text)
    cleaned_text = ' '.join(cleaned_text.split())      
    return cleaned_text

def clean_content(text: str):
    return ' '.join([w.lower() for w in text.split() if w.isalpha()])
