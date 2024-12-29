
from fastapi import APIRouter
from app.api.v1.handlers import pdfRouter, filesRouter
from app.constants import routes

api_router_v1 = APIRouter()

api_router_v1.include_router(pdfRouter, prefix = routes.PROCCES_PDFS, tags=["pdf"])
api_router_v1.include_router(filesRouter, tags=["files"])