from fastapi import APIRouter, Depends, File, UploadFile
from typing import List

from app.services import file_service, FileService

router = APIRouter()

@router.post("/upload")
async def upload_file(
    files: List[UploadFile] = File(...),
    file_service: FileService = Depends(lambda: file_service) 
):
    key = await file_service.save_files(files)
    return {
        "status": "Files uploaded successfully",
        "key": key
    }
