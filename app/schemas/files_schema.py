from pydantic import BaseModel
from typing import List
from uuid import UUID

class UploadFilesResponse(BaseModel):
    status: str
    token: UUID
    type_files: str

class DownloadFilesResponse(BaseModel):
    status: str
    file_names: List[str]