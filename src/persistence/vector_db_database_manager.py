from src.domain.utilities.logger import logger
from src.domain.utilities.settings import SETTINGS
from src.domain.utilities.singleton import Singleton
import qdrant_client


class VectorDBDatabaseManager(metaclass=Singleton):
	"""
	Utility class to manage Vector database connection.

	:param AsyncQdrantClient async_client: asynchronous Qdrant client.
	:param QdrantClient sync_client: synchronous Qdrant client.
	"""

	def __init__(self):
		"""
		Initialize Vector database synchronous and asynchronous clients.
		"""

		self.async_client = qdrant_client.AsyncQdrantClient(
			location=SETTINGS.VECTOR_DB_HOST,
			port=SETTINGS.VECTOR_DB_PORT,
			api_key=SETTINGS.VECTOR_DB_APIKEY,
			https=False,
		)

		self.sync_client = qdrant_client.QdrantClient(
			location=SETTINGS.VECTOR_DB_HOST,
			port=SETTINGS.VECTOR_DB_PORT,
			api_key=SETTINGS.VECTOR_DB_APIKEY,
			https=False,
		)

	def get_async_client(self) -> qdrant_client.AsyncQdrantClient:
		"""
		Retrieve an asynchronous Vector database client to perform operations on the Vector database.

		:return: An asynchronous client to make operations on the Vector database.
		:rtype: AsyncQdrantClient
		"""

		logger.info(msg="Start")

		return self.async_client

	def get_sync_client(self) -> qdrant_client.QdrantClient:
		"""
		Retrieve a synchronous Vector database client to perform operations on the Vector database.

		:return: A synchronous client to make operations on the Vector database.
		:rtype: QdrantClient
		"""

		logger.debug(msg="Start")

		return self.sync_client

	@staticmethod
	def get_collection(type: str) -> str:
		"""
		Return the collection related to the given type.

		:param str type: object type, as string.
		:return: the name of the collection related to the given type.
		:rtype: str
		"""

		logger.debug(msg="Start")

		match type:
			case "VectorDatabaseTemplateEntity":
				return SETTINGS.VECTOR_DB_COLLECTION_NAME
			case _:
				return ""
