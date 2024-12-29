class Routes:
    HEALTH_CHECK = "/health-check"
    PROCCES_PDFS = "/process-pdfs"
    V1 = "/v1"

    FILES = "/files"
    UPLOAD_FILES = f"{FILES}/upload"
    DOWNLOAD_FILES = f"{FILES}/download"


routes = Routes()
