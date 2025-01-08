from neomodel import config

from src.domain.utilities.settings import SETTINGS


class GraphDatabaseManager:
	"""
	Utility class to manage connection to Graph database connection.
	"""

	def __init__(self):
		"""
		Initialize the connection to Graph database.
		"""

		config.DATABASE_URL = f"bolt://{SETTINGS.GRAPH_DB_USER}:{SETTINGS.GRAPH_DB_PASSWORD}@{SETTINGS.GRAPH_DB_HOST}:{SETTINGS.GRAPH_DB_PORT}"
