
from elasticsearch.helpers import bulk

from app.core.database import get_connection
from app.core.elasticsearch import get_elasticsearch
from app.core.search_index import INDEX_NAME

# Перенос документов из SQL Server
def index_documents():
    es = get_elasticsearch()
    connection = get_connection()
    cursor = connection.cursor()

    rows = cursor.execute("""
        SELECT
            d.id,
            d.title,
            d.content,
            dep.name AS department,
            al.name AS access_level,
            d.author_id
        FROM Documents d
        JOIN Departments dep ON d.department_id = dep.id
        JOIN AccessLevels al ON d.access_level_id = al.id
    """).fetchall()

    actions = []

    for row in rows:
        actions.append({
            "_index": INDEX_NAME,
            "_id": row.id,
            "_source": {
                "document_id": row.id,
                "title": row.title,
                "content": row.content,
                "department": row.department,
                "access_level": row.access_level,
                "author_id": row.author_id
            }
        })

    success, errors = bulk(es, actions)

    connection.close()

    print(f"Проиндексировано документов: {success}")

    if errors:
        print("Ошибки при индексации:", errors)


if __name__ == "__main__":
    index_documents()
