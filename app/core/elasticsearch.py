
import urllib3
from elasticsearch import Elasticsearch

from app.core.config import (
    ELASTICSEARCH_URL,
    ELASTICSEARCH_USER,
    ELASTICSEARCH_PASSWORD,
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

es = Elasticsearch(
    ELASTICSEARCH_URL,
    basic_auth=(ELASTICSEARCH_USER, ELASTICSEARCH_PASSWORD),
    verify_certs=False,
)

def get_elasticsearch():
    return es
