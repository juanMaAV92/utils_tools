import json
from typing import List

from fastapi import APIRouter, Body, File, Form, UploadFile

from app.schemas import PDFBody

router = APIRouter()


@router.post("")
async def process_pdf(body: str = Form(...), files: List[UploadFile] = File(...)):
    body = json.loads(body)
    pdf_body = PDFBody(**body)

    for pdf_file in body:
        print(f"Processing file: {pdf_file.file_name}")
        for operation in pdf_file.operations:
            print(
                f"Operation: {operation.operation}, Pages: {operation.pages}, Angle: {operation.angle}"
            )

    return {"status": "ok", "file_count": len(files), "body": body}
