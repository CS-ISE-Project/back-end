from app.config.creds import ELASTICSEARCH_URL, ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD,INDEX_NAME

from elasticsearch import Elasticsearch
    
es = Elasticsearch(
    ELASTICSEARCH_URL,
    http_auth=(ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD)
)
try:
    resp = es.indices.put_mapping(
        index=INDEX_NAME,
        body={
            "properties": {
                "url": {"type": "text"},
                "title": {"type": "text"},
                "authors": {"type": "text"},
                "institutes": {"type": "text"},
                "keywords": {"type": "text"},
                "abstract": {"type": "text"},
                "content": {"type": "text"},
                "references": {"type": "text"},
                "publication_date": {"type": "date"}
            }
        },
    )
    if resp.get("acknowledged"):
        print("Index mapped successfully")
except Exception as e:
    print("An error occurred while mapping the index :", e)
