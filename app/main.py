import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.core import settings
from app.constants import routes
from app.api import api_router_v1

app = FastAPI(
    title= settings.APP_NAME,
    version= settings.APP_VERSION,

    docs_url= settings.APP_DOC_URL,
    openapi_url= f"/{settings.APP_VERSION}/openapi.json",
)

@app.get(routes.HEALTH_CHECK, tags=["health"])
async def health_check():
    return JSONResponse(content={"status": "ok"})

app.include_router(api_router_v1, prefix= routes.V1)

def run():
    uvicorn.run(
        "app.main:app",
        host= settings.SERVER_HOST,
        port= settings.SERVER_PORT,
        reload= settings.APP_RELOAD,
        log_level= settings.DEBUG
    )    

if __name__ == "__main__":
    run()
