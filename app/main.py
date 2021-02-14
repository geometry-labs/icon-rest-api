from threading import Thread

import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.routes.v1.router import api_router

app = FastAPI(openapi_url=f"{settings.API_ENDPOINT_PREFIX}/openapi.json")

app.include_router(api_router, prefix=settings.API_ENDPOINT_PREFIX)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", log_level="info", debug=True, workers=1)
