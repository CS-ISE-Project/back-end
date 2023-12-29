import re

def clean_text(text):
    cleaned_text = re.sub(r'[^\w\s.,:?!\'"-+=()[\]{}*&%$#@;/|]', '', text)
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text