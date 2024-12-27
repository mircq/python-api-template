from motor.motor_asyncio import AsyncIOMotorClient

from src.domain.utilities.logger import logger
from src.domain.utilities.settings import SETTINGS
from src.domain.utilities.singleton import Singleton

from beanie import init_beanie

from src.persistence.objects.nosql_template import NoSQLTemplate


class NoSQLDatabaseManager(metaclass=Singleton):
	"""
	Utility class to manage connection to NoSQL database connection.
	"""

	def __init__(self):
		"""
		Initialize the connection to NoSQL database.
		"""

		logger.info(msg="Start")

		self.async_client = AsyncIOMotorClient(
			f"mongodb://{SETTINGS.NOSQL_DB_USER}:{SETTINGS.NOSQL_DB_PASSWORD}@{SETTINGS.NOSQL_DB_HOST}:{SETTINGS.NOSQL_DB_PORT}/{SETTINGS.NOSQL_DB_NAME}"
		)

		logger.info(msg="End")

	async def create_tables(self) -> None:
		"""
		Create NoSQL database tables.
		"""

		logger.info(msg="Start")

		# Initialize beanie with the Product document class
		await init_beanie(database=self.async_client.db_name, document_models=[NoSQLTemplate])

		logger.info(msg="End")

	def get_session(self):
		""" """

		return self.async_client.start_session()
