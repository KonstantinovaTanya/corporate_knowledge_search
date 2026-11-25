
from app.core.database import get_connection


def get_all_documents():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        rows = cursor.execute(
            """
            SELECT
                d.id,
                d.title,
                d.filename,
                dep.name AS department,
                al.name AS access_level,
                d.author_id
            FROM Documents d
            JOIN Departments dep
                ON d.department_id = dep.id
            JOIN AccessLevels al
                ON d.access_level_id = al.id
            ORDER BY d.id DESC
            """
        ).fetchall()

        documents = []

        for row in rows:
            documents.append({
                "id": row.id,
                "title": row.title,
                "filename": row.filename,
                "department": row.department,
                "access_level": row.access_level,
                "author_id": row.author_id
            })

        return documents

    finally:
        connection.close()


def get_document_by_id(document_id: int):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        row = cursor.execute(
            """
            SELECT
                d.id,
                d.title,
                d.filename,
                d.content,
                dep.name AS department,
                al.name AS access_level,
                d.author_id
            FROM Documents d
            JOIN Departments dep
                ON d.department_id = dep.id
            JOIN AccessLevels al
                ON d.access_level_id = al.id
            WHERE d.id = ?
            """,
            document_id
        ).fetchone()

        if not row:
            return None

        return {
            "id": row.id,
            "title": row.title,
            "filename": row.filename,
            "content": row.content,
            "department": row.department,
            "access_level": row.access_level,
            "author_id": row.author_id
        }

    finally:
        connection.close()
