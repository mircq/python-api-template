import uvicorn
from fastapi import FastAPI

from src.domain.utilities.settings import settings
from src.presentation.endpoints.templates.template_endpoints import template_router

app = FastAPI(
    title="Template microservice",
    summary="This is a simple Python template for a backend microservice.",
    description="The templates offers the possibility to perform simple CRUD operations.",
    docs_url="/docs",
    version="1.0"
)

app.include_router(router=template_router)

uvicorn.run(app=app, host="0.0.0.0", port=settings.port)