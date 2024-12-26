import json
import os
import uuid
import aiofiles
from typing import List
from fastapi import UploadFile

from app.services.redis_service import redis_service


TEMP_DIR = "/tmp"

class FileService:
    def __init__(self):
        if not os.path.exists(TEMP_DIR):
            os.makedirs(TEMP_DIR)

    async def save_files(self, files: List[UploadFile]) -> str:
        file_paths = []
        for file in files:
            file_path = f"{TEMP_DIR}/{file.filename}"
            async with aiofiles.open(file_path, "wb") as buffer:
                data = await file.read()
                await buffer.write(data)
            file_paths.append(file_path)
    
        key = str(uuid.uuid4())

        file_paths_json = json.dumps(file_paths)
        await redis_service.set(key, file_paths_json)
        return key
    
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