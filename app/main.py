import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.routes.v1.router import api_router

tags_metadata = [
    {
        "name": "blocks",
        "description": "Get block data.",
    },
    {
        "name": "transactions",
        "description": "Get transaction data.",
    },
    {
        "name": "contract events",
        "description": "Get event log data.",
    },
]


app = FastAPI(
    title="ICON Blockchain REST API",
    description="Retrieve block, transaction, and event log data.",
    version="v0.1.0",
    openapi_tags=tags_metadata,
    openapi_url=f"{settings.ICON_REST_API_PREFIX}/openapi.json",
    docs_url=f"{settings.ICON_REST_API_PREFIX}/docs",
)

app.include_router(api_router, prefix=settings.ICON_REST_API_PREFIX)

if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="0.0.0.0", port=settings.ICON_REST_API_PORT , log_level="info", debug=True, workers=1
    )  # TODO: 1 worker?
