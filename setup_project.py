
from app.core.init_db import init_database
from app.core.import_documents import import_documents
from app.core.search_index import create_search_index
from app.core.index_documents import index_documents


def setup_project():
    steps = [
        ("Создание базы данных и таблиц", init_database),
        ("Импорт тестовых документов в SQL Server", import_documents),
        ("Создание индекса Elasticsearch", create_search_index),
        ("Индексация документов в Elasticsearch", index_documents),
    ]

    for step_name, step_function in steps:
        print(f"\n--- {step_name} ---")
        step_function()
        print("Выполнено успешно.")

    print("\nПодготовка проекта завершена!")


if __name__ == "__main__":
    setup_project()
