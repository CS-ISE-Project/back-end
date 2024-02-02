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
    d_m_y = date_string.split('-')
    return date(int(d_m_y[2]), int(d_m_y[1]), int(d_m_y[0]))
