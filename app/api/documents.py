
from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from app.services.document_upload_service import extract_text
from app.services.document_storage_service import save_document
from app.core.index_documents import index_single_document
from app.services.document_query_service import (
    get_all_documents,
    get_document_by_id
)
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 МБ

router = APIRouter(
    prefix="/documents",
    tags=["Документы"]
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    title: str = Form(...),
    department: str = Form(...),
    access_level: str = Form(...)
):
    extension = Path(file.filename).suffix.lower()

    if extension not in [".pdf", ".docx"]:
        raise HTTPException(
            status_code=400,
            detail="Поддерживаются только PDF и DOCX"
        )

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Размер файла не должен превышать 20 МБ"
        )

    if not content:
        raise HTTPException(
            status_code=400,
            detail="Файл пустой"
        )

    try:
        text = extract_text(file.filename, content)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Не удалось прочитать файл"
        )

    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="В файле отсутствует текст"
        )

    if not title.strip():
        raise HTTPException(
            status_code=400,
            detail="Название документа не может быть пустым"
        )

    if access_level not in ["all", "department", "admin"]:
        raise HTTPException(
            status_code=400,
            detail="Некорректный уровень доступа"
        )

    if department not in [
        "HR",
        "Finance",
        "IT",
        "Sales",
        "Administrative"
    ]:
        raise HTTPException(
            status_code=400,
            detail="Неизвестное подразделение"
        )

    try:
        document_id = save_document(
            filename=file.filename,
            title=title,
            content=text,
            department=department,
            access_level=access_level
        )
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Ошибка при сохранении документа"
        )

    try:
        index_single_document(document_id)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Документ сохранён в базе данных, но не удалось добавить его в поисковый индекс"
        )

    return {
        "message": "Документ успешно загружен",
        "document_id": document_id,
        "filename": file.filename,
        "title": title,
        "department": department,
        "access_level": access_level,
        "format": extension,
        "characters": len(text)
    }


@router.get("/")
def get_documents():
    try:
        documents = get_all_documents()

        return {
            "total": len(documents),
            "documents": documents
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Не удалось получить список документов"
        )


@router.get("/{document_id}")
def get_document(document_id: int):
    try:
        document = get_document_by_id(document_id)

        if document is None:
            raise HTTPException(
                status_code=404,
                detail="Документ не найден"
            )

        return document

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Не удалось получить документ"
        )
