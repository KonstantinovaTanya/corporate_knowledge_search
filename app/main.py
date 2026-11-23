
from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
from io import BytesIO
import fitz
from docx import Document


from app.core.config import (
    APP_NAME,
    APP_DESCRIPTION,
    APP_VERSION,
    APP_ENV
)


# Создаём приложение FastAPI
app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)


@app.get("/")
def read_root():
    return {
        "message": "Корпоративная система поиска знаний работает!",
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV
    }


@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    extension = Path(file.filename).suffix.lower()

    if extension not in [".pdf", ".docx"]:
        raise HTTPException(status_code=400, detail="Поддерживаются только PDF и DOCX")

    content = await file.read()

    if not content:
        raise HTTPException(status_code=400, detail="Файл пустой")
    
    if extension == ".pdf":
        pdf = fitz.open(stream=content, filetype="pdf")
        text = "\n".join(page.get_text() for page in pdf)
        pdf.close()
    elif extension == ".docx":
        document = Document(BytesIO(content))
        text = "\n".join(paragraph.text for paragraph in document.paragraphs)
    
    return {
        "filename": file.filename,
        "format": extension,
        "text": text,
        "characters": len(text)
    }