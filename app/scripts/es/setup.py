from app.config.creds import ELASTICSEARCH_URL, ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD 

from elasticsearch import Elasticsearch
    
es = Elasticsearch(
    ELASTICSEARCH_URL,
    http_auth=(ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD)
)