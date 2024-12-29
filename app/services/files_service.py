import json
import os
import uuid
import aiofiles
from typing import List
from fastapi import UploadFile, HTTPException
from dataclasses import dataclass
from uuid import UUID

from app.services.redis_service import redis_service
from app.utils import verify_file_types

TEMP_DIR = "/tmp"

@dataclass
class SaveFilesResult:
    token: UUID
    file_type: str

class FileService:
    def __init__(self):
        if not os.path.exists(TEMP_DIR):
            os.makedirs(TEMP_DIR)

    async def get_files(self, token: UUID) -> List[str]:
        file_paths_json = await redis_service.get(str(token))
        if not file_paths_json:
            raise HTTPException(status_code=404, detail="Files not found")
        file_names = [os.path.basename(file_path) for file_path in json.loads(file_paths_json)]
        
        return file_names



    async def save_files(self, files: List[UploadFile]) -> SaveFilesResult:
        error, file_type = verify_file_types(files)
        if error:
            raise HTTPException(status_code=400, detail=error)

        file_paths = []
        for file in files:
            file_path = f"{TEMP_DIR}/{file.filename}"
            async with aiofiles.open(file_path, "wb") as buffer:
                data = await file.read()
                await buffer.write(data)
            file_paths.append(file_path)
    
        token = uuid.uuid4()
        file_paths_json = json.dumps(file_paths)
        await redis_service.set(str(token), file_paths_json)

        return SaveFilesResult(token=token, file_type=file_type)
    
    async def delete_files(self, key: str) -> None:
        file_paths_json = await redis_service.get(key)
        if file_paths_json:
            file_paths = json.loads(file_paths_json)
            for file_path in file_paths:
                os.remove(file_path)
            await redis_service.delete(key)
        else:
            raise Exception("Files not found")  
        
file_service = FileService()