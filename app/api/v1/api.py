from fastapi import APIRouter

from app.api.v1.handlers import filesRouter

api_router_v1 = APIRouter()

api_router_v1.include_router(filesRouter, tags=["files"])
