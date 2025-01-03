from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, File, Query, UploadFile
from fastapi.responses import JSONResponse

from app.constants.routes import Routes
from app.schemas import DownloadFilesResponse, UploadFilesResponse
from app.services import FileService, file_service

router = APIRouter()


@router.post(
    Routes.UPLOAD_FILES,
    response_model=UploadFilesResponse,
)
async def upload_file(
    files: List[UploadFile] = File(...),
    file_service: FileService = Depends(lambda: file_service),
):
    result = await file_service.save_files(files)
    return JSONResponse(
        content=UploadFilesResponse(
            status="success", token=result.token, type_files=result.file_type
        ).model_dump(),
        status_code=201,
        media_type="application/json",
    )


@router.get(Routes.DOWNLOAD_FILES, response_model=DownloadFilesResponse)
async def download_files(
    token: UUID = Query(..., description="The token generated by the upload endpoint"),
    file_service: FileService = Depends(lambda: file_service),
):
    file_names = await file_service.get_files(token)

    return JSONResponse(
        content=DownloadFilesResponse(
            status="success", file_names=file_names
        ).model_dump(),
        status_code=200,
        media_type="application/json",
    )
