from pydantic import BaseModel
from typing import List

class Operation(BaseModel):
    operation: str
    pages: List[int]
    angle: int = None

class PDFFile(BaseModel):
    file_name: str
    operations: List[Operation]

class PDFBody(BaseModel):
    pdfs: List[PDFFile]