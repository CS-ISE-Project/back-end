from app.config.creds import INDEX_NAME

from app.scripts.es.setup import es

es.delete_by_query(index=INDEX_NAME, body={"query": {"match_all": {}}})
print("Index cleared successfully")

es.indices.put_mapping(
    index= INDEX_NAME,
    body= {
        "properties": {
            "url": {"type": "text"},
            "publication_date": {"type": "date"},
            "title": {"type": "text"},
            "authors": {"type": "text"},
            "institutes": {"type": "text"},
            "keywords": {"type": "text"},
            "abstract": {"type": "text"},
            "content": {"type": "text"},
            "references": {"type": "text"}
        }
    }
)
print("Index mapped successfully")
