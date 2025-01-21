import os
from app.schemas import ProcessRequest
from app.interfaces import FileProcessor, ProcessedFile

TEMP_DIR = "/tmp"

class PDFProcessor(FileProcessor):
    async def process(self, request: ProcessRequest) -> ProcessedFile:
        output_pdf_path = os.path.join(TEMP_DIR, "output.pdf")
        # Simulación de la creación del archivo PDF
        with open(output_pdf_path, "wb") as f:
            f.write(b"%PDF-1.4\n%...")  # Contenido simulado de un archivo PDF
        return ProcessedFile(
            path=output_pdf_path,
            filename="output.pdf",
            media_type="application/pdf",
        )
    

