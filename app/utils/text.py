import re

from datetime import date

def clean_text(text: str):
    cleaned_text = re.sub(r'[^\w\s.,:;/?!\'"-–_+=()[\]{}*%$@]', '', text)
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text

def clean_content(text: str):
    return ' '.join([w.lower() for w in text.split() if w.isalpha()])

def is_date(date_string):
    return re.match(r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}', date_string) is not None

def get_date(date_string):
    if is_date(date_string):
        return date(*[int(x) for x in date_string.split('-')][::-1])
    else:
        return None

def get_es_date(date_string):
    if is_date(date_string):
        d, m, y = date_string.split('-')
        d = '0' + d if len(d) == 1 else d
        m = '0' + m if len(m) == 1 else m
        return f'{y}-{m}-{d}'
    else:
        return None