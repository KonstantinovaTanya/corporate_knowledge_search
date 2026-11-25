
from app.core.elasticsearch import get_elasticsearch

INDEX_NAME = "corporate_documents"

INDEX_SETTINGS = {
    "analysis": {
        "analyzer": {
            "russian_analyzer": {
                "type": "russian"
            }
        }
    }
}

INDEX_MAPPINGS = {
    "properties": {
        "document_id": {"type": "keyword"},
        "title": {
            "type": "text",
            "analyzer": "russian_analyzer"
        },
        "content": {
            "type": "text",
            "analyzer": "russian_analyzer"
        },
        "department": {"type": "keyword"},
        "access_level": {"type": "keyword"},
        "author_id": {"type": "keyword"}
    }
}

# Создание поискового индекса
def create_search_index():
    es = get_elasticsearch()

    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(
            index=INDEX_NAME,
            settings=INDEX_SETTINGS,
            mappings=INDEX_MAPPINGS
        )

        print(f"Индекс {INDEX_NAME} успешно создан.")
    else:
        print(f"Индекс {INDEX_NAME} уже существует.")
