import uvicorn
from fastapi import FastAPI

from src.presentation.endpoints.template_endpoints import template_router

app = FastAPI(
    title="Template microservice",
    summary="Template microservice summary",
    description="Template microservice description",
    docs_url="/docs",
)

app.include_router(router=template_router)

uvicorn.run(app=app, host="0.0.0.0", port=8000)