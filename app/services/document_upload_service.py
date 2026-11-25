
from pathlib import Path
from io import BytesIO

import fitz
from docx import Document


def extract_text(filename: str, content: bytes) -> str:
    extension = Path(filename).suffix.lower()

    if extension == ".pdf":
        pdf = fitz.open(stream=content, filetype="pdf")
        try:
            return "\n".join(page.get_text() for page in pdf)
        finally:
            pdf.close()

    if extension == ".docx":
        document = Document(BytesIO(content))
        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

    raise ValueError("Поддерживаются только PDF и DOCX")
