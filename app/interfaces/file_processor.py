from abc import ABC, abstractmethod
from dataclasses import dataclass
from app.schemas import ProcessRequest


@dataclass
class ProcessedFile:
    path: str
    filename: str
    media_type: str

    
class FileProcessor(ABC):
    @abstractmethod
    async def process(self, request: ProcessRequest) -> ProcessedFile:
        pass