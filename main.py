from threading import Thread

import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.routes.v1.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="0.0.0.0", port=8000, log_level="info", debug=True, workers=1
    )

