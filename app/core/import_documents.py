
from pathlib import Path

import fitz
from docx import Document as DocxDocument

from app.core.database import get_connection


BASE_DIR = Path(__file__).resolve().parents[2]
DOCUMENTS_DIR = BASE_DIR / "documents" / "samples"
REGISTRY_PATH = BASE_DIR / "tests" / "document_registry.md"


def read_registry():
    """Читает реестр документов из Markdown."""

    documents = []

    with open(REGISTRY_PATH, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line.startswith("|") or line.startswith("| --"):
                continue

            cells = [cell.strip() for cell in line.strip("|").split("|")]

            if len(cells) != 5 or cells[0] == "ID":
                continue

            document_id, filename, title, department, access_level = cells

            documents.append({
                "id": document_id,
                "filename": filename,
                "title": title,
                "department": department,
                "access_level": access_level
            })

    return documents


def extract_text(file_path):
    """Извлекает текст из PDF или DOCX."""

    if file_path.suffix.lower() == ".pdf":
        with fitz.open(file_path) as pdf:
            return "\n".join(page.get_text() for page in pdf)

    if file_path.suffix.lower() == ".docx":
        doc = DocxDocument(file_path)

        parts = [paragraph.text for paragraph in doc.paragraphs]

        for table in doc.tables:
            for row in table.rows:
                parts.append(" | ".join(cell.text for cell in row.cells))

        return "\n".join(parts)

    raise ValueError(f"Неподдерживаемый формат: {file_path.suffix}")


def import_documents():
    """Импортирует и обновляет документы в SQL Server."""

    documents = read_registry()

    connection = get_connection()
    cursor = connection.cursor()

    imported = 0
    updated = 0

    try:
        for item in documents:
            document_id = item["id"]
            filename = item["filename"]
            title = item["title"]
            department = item["department"]
            access_level = item["access_level"]

            file_path = DOCUMENTS_DIR / filename

            if not file_path.exists():
                raise FileNotFoundError(
                    f"Файл не найден: {file_path}"
                )

            content = extract_text(file_path)

            cursor.execute(
                """
                IF NOT EXISTS (
                    SELECT 1 FROM Departments WHERE name = ?
                )
                INSERT INTO Departments (name) VALUES (?)
                """,
                department,
                department
            )

            cursor.execute(
                "SELECT id FROM Departments WHERE name = ?",
                department
            )
            department_id = cursor.fetchone()[0]

            cursor.execute(
                "SELECT id FROM AccessLevels WHERE name = ?",
                access_level
            )
            result = cursor.fetchone()

            if result is None:
                raise ValueError(
                    f"Неизвестный уровень доступа: {access_level}"
                )

            access_level_id = result[0]

            cursor.execute(
                "SELECT id FROM Documents WHERE id = ?",
                document_id
            )

            if cursor.fetchone():
                cursor.execute(
                    """
                    UPDATE Documents
                    SET
                        title = ?,
                        filename = ?,
                        department_id = ?,
                        access_level_id = ?,
                        content = ?
                    WHERE id = ?
                    """,
                    title,
                    filename,
                    department_id,
                    access_level_id,
                    content,
                    document_id
                )

                updated += 1

            else:
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
                    VALUES (?, ?, ?, ?, ?, NULL, ?)
                    """,
                    document_id,
                    title,
                    filename,
                    department_id,
                    access_level_id,
                    content
                )

                imported += 1

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    print(f"Новых документов добавлено: {imported}")
    print(f"Существующих документов обновлено: {updated}")
    print(f"Всего обработано: {len(documents)}")


if __name__ == "__main__":
    import_documents()
