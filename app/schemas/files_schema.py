from typing import List
from uuid import UUID

from pydantic import BaseModel


class UploadFilesResponse(BaseModel):
    status: str
    token: UUID
    type_files: str


class DownloadFilesResponse(BaseModel):
    status: str
    file_names: List[str]
