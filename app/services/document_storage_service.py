from app.core.database import get_connection


def save_document(
    filename: str,
    title: str,
    content: str,
    department: str,
    access_level: str,
    author_id: str | None = None
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        # Получаем следующий номер документа
        next_number = cursor.execute("""
            SELECT ISNULL(
                MAX(TRY_CONVERT(INT, SUBSTRING(id, 4, 17))),
                0
            ) + 1 AS next_number
            FROM Documents WITH (UPDLOCK, HOLDLOCK)
            WHERE id LIKE 'DOC%'
        """).fetchone().next_number

        document_id = f"DOC{next_number:03d}"

        # Получаем ID подразделения
        department_row = cursor.execute(
            """
            SELECT id
            FROM Departments
            WHERE name = ?
            """,
            department
        ).fetchone()

        if not department_row:
            raise ValueError(
                f"Подразделение '{department}' не найдено"
            )

        # Получаем ID уровня доступа
        access_row = cursor.execute(
            """
            SELECT id
            FROM AccessLevels
            WHERE name = ?
            """,
            access_level
        ).fetchone()

        if not access_row:
            raise ValueError(
                f"Уровень доступа '{access_level}' не найден"
            )

        # Сохраняем документ
        cursor.execute(
            """
            INSERT INTO Documents (
                id,
                title,
                filename,
                department_id,
                access_level_id,
                author_id,
                content
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            document_id,
            title,
            filename,
            department_row.id,
            access_row.id,
            author_id,
            content
        )

        connection.commit()

        return document_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()