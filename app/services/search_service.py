
from app.core.elasticsearch import get_elasticsearch
from app.core.search_index import INDEX_NAME
from app.models.user import User
from app.models.enums import UserRole


def search_documents(user: User, query: str, size: int = 10):
    es = get_elasticsearch()

    search_query = {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": query,
                        "fields": ["title^3", "content"]
                    }
                }
            ]
        }
    }

    # Администратор видит все документы.
    if user.role != UserRole.ADMIN:
        search_query["bool"]["filter"] = [
            {
                "bool": {
                    "should": [
                        {"term": {"access_level": "all"}},
                        {
                            "bool": {
                                "must": [
                                    {"term": {"access_level": "department"}},
                                    {"term": {"department": user.department}}
                                ]
                            }
                        }
                    ],
                    "minimum_should_match": 1
                }
            }
        ]

    response = es.search(
        index=INDEX_NAME,
        query=search_query,
        size=size
    )

    results = []

    for hit in response["hits"]["hits"]:
        document = hit["_source"].copy()
        document["score"] = hit["_score"]
        results.append(document)

    return results
