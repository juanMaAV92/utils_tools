
from fastapi import APIRouter
from app.api.v1.handlers import pdf
from app.constants import routes
from .handlers import *

api_router_v1 = APIRouter()

api_router_v1.include_router(pdf.router, prefix = routes.PROCCES_PDFS, tags=["pdf"])