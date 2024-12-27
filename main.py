from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.domain.utilities.logger import logger
from src.domain.utilities.settings import SETTINGS
from src.infrastructure.clients.langchain_client import LangchainClient
from src.persistence.objects.template import Template # DO NOT REMOVE: this import makes the code create the table on the db.
from src.persistence.sql_database_manager import SQLDatabaseManager
from src.persistence.vector_db_database_manager import VectorDBDatabaseManager
from src.presentation.endpoints.health.health_endpoints import health_router

from src.presentation.endpoints.templates.template_endpoints import template_router


# TODO it is incorrect to directly call persistence (?)
@asynccontextmanager
async def lifespan(app: FastAPI):
	"""
	Define startup and cleanup operations for a FastAPI app.

	:param FastAPI app: FastAPI app to
	"""

	# TODO evaluate if moving these lines into the init of persistence or infrastructure and simply import them here

	# Initialize SQL database connection and create tables
	logger.info(msg="Initializing SQL database connection.")
	#await SQLDatabaseManager().create_tables()
	logger.info(msg="SQL database connection correctly initialized.")

	# Initialize Vector database connection
	logger.info(msg="Initializing Vector database connection.")
	#VectorDBDatabaseManager()
	logger.info(msg="Vector database connection correctly initialized.")

	# Initialize Langchain agent
	logger.info(msg="Initializing Langchain agent.")
	LangchainClient()
	logger.info(msg="Langchain agent correctly initialized.")

	logger.info(msg="App is now ready to manage requests.")

	yield


app = FastAPI(
	title="Python API Template",
	summary="This is a template backend written in Python.",
	description="The swagger offers the possibility to perform simple CRUD operations.",
	docs_url="/docs",
	version="1.0",
	lifespan=lifespan,
)

# Include endpoints routers
app.include_router(router=health_router)
app.include_router(router=template_router)

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


logger.info(msg=f"Starting server on 0.0.0.0:{SETTINGS.PORT}")

uvicorn.run(app=app, host="0.0.0.0", port=SETTINGS.PORT, log_level="error")
