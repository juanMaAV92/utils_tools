from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, field_validator


class Operation(BaseModel):
    file_name: str
    operation: str
    pages: List[int]
    angle: Optional[int] = None

    @field_validator('operation')
    def validate_operation(cls, v):
        if v not in {'rotate', 'delete'}:
            raise ValueError('Operation must be either "rotate" or "delete"')
        return v
    
    @field_validator('angle', mode='before')
    def validate_angle(cls, v, values):
        if values.data.get('operation') == 'rotate' and v is None:
            raise ValueError('Angle must be provided for rotate operations')
        return v



class ProcessRequest(BaseModel):
    token: UUID
    files_type: str
    operations: List[Operation]

    @field_validator('files_type', mode='before')
    def validate_files_type(cls, v):
        if v not in {'pdf'}:
            raise ValueError("Files type must be pdf")
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "token": "123e4567-e89b-12d3-a456-426614174000",
                "files_type": "pdf",
                "operations": [
                    {
                        "file_name": "file1.pdf",
                        "operation": "rotate",
                        "pages": [1, 2, 3],
                        "angle": 90
                    },
                    {
                        "file_name": "file2.pdf",
                        "operation": "delete",
                        "pages": [1, 2, 3]
                    }
                ]
            }
        }

