from app.config.creds import ELASTICSEARCH_HOST,ELASTICSEARCH_PASSWORD,ELASTICSEARCH_PORT,ELASTICSEARCH_SCHEME,ELASTICSEARCH_USERNAME
from elasticsearch import Elasticsearch

def get_es_instance():
    return Elasticsearch(
        [
            {'host': ELASTICSEARCH_HOST, 'port': int(ELASTICSEARCH_PORT), "scheme": ELASTICSEARCH_SCHEME}
        ],
            basic_auth=(ELASTICSEARCH_USERNAME, ELASTICSEARCH_PASSWORD)
    )
