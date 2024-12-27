import uuid
from datetime import datetime

from src.domain.entities.vector_database_template_entity import VectorDatabaseTemplateEntity
from src.domain.entities.vector_database_template_payload_entity import VectorDatabaseTemplatePayloadEntity
from src.domain.results.result import Result
from src.domain.utilities.constants import date_format
from src.domain.utilities.exception_handler import exception_handler
from src.domain.utilities.logger import logger
from src.domain.utilities.settings import SETTINGS
from src.domain.utilities.singleton import Singleton
from langchain_ollama.llms import OllamaLLM
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter




class LangchainClient(metaclass=Singleton):
	"""
	Utility class to manage Langchain connection.

	"""

	def __init__(self):
		"""
		Create retrieval document chain using embedder and llm specified in environment variables.
		"""

		logger.info(msg="Start")

		logger.info(
			msg=f"Initializing connection to LLM with base_url={SETTINGS.LLM_HOST}:{SETTINGS.LLM_PORT} and model={SETTINGS.LLM_NAME}"
		)
		self.embedder = OllamaEmbeddings(base_url=f"{SETTINGS.EMBEDDER_HOST}:{SETTINGS.EMBEDDER_PORT}", model=SETTINGS.EMBEDDER_NAME)

	@exception_handler
	async def embed(self, text: str, chunk_size: int = 1024, chunk_overlap: int = 128) -> Result[list[VectorDatabaseTemplateEntity]]:
		"""

		"""

		logger.info(msg="Start")

		text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

		chunks: list[str] = text_splitter.split_text(text=text)

		result: [VectorDatabaseTemplateEntity] = []

		for chunk in chunks:

			vector: list[float] = await self.embedder.aembed_query(text=chunk)

			result.append(
				VectorDatabaseTemplateEntity(
					id=str(uuid.uuid4()),
					vector=vector,
					payload=VectorDatabaseTemplatePayloadEntity(
						text=chunk,
						upload_date=datetime.now().strftime(format=date_format)
					)
				)
			)

		logger.info(msg="End")

		return Result.ok(value=result)


