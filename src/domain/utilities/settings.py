from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	PORT: int = Field(title="PORT", description="Port on which the microservice is exposed.", default=8000)

	LOG_LEVEL: Literal["debug", "info", "warning", "error"] = Field(
		title="LOG_LEVEL", description="Level for log display.", default="info"
	)

	# region RELATIONAL_DB

	RELATIONAL_DB_TYPE: str | None = Field(
		title="RELATIONAL_DB_TYPE", description="Type of relational database used.", default=None
	)

	RELATIONAL_DB_HOST: str | None = Field(
		title="RELATIONAL_DB_HOST", description="Host on which the relational database is deployed.", default=None
	)

	RELATIONAL_DB_PORT: str | None = Field(
		title="RELATIONAL_DB_PORT", description="Port on which the relational database is exposed.", default=None
	)

	RELATIONAL_DB_USER: str | None = Field(
		title="RELATIONAL_DB_USER", description="Username for accessing relational database.", default=None
	)

	RELATIONAL_DB_PASSWORD: str | None = Field(
		title="RELATIONAL_DB_PASSWORD", description="Password for accessing relational database.", default=None
	)

	RELATIONAL_DB_NAME: str | None = Field(
		title="RELATIONAL_DB_NAME", description="Name of the relational database.", default=None
	)

	# endregion

	# region VECTOR_DB

	VECTOR_DB_HOST: str | None = Field(
		title="VECTOR_DB_HOST", description="Host on which the vector database is deployed.", default=None
	)

	VECTOR_DB_PORT: str | None = Field(
		title="VECTOR_DB_PORT", description="Port on which the vector database is exposed.", default=None
	)

	VECTOR_DB_APIKEY: str | None = Field(
		title="VECTOR_DB_APIKEY", description="Api key for accessing vector database.", default=None
	)

	# endregion

	# region KEY_VALUE_DB

	REDIS_DB_HOST: str | None = Field(
		title="REDIS_DB_HOST", description="Host on which the Redis database is deployed.", default=None
	)

	REDIS_DB_USER: str | None = Field(
		title="REDIS_DB_USER", description="Username for accessing Redis database.", default=None
	)

	REDIS_DB_PASSWORD: str | None = Field(
		title="REDIS_DB_PASSWORD", description="Password for accessing Redis database.", default=None
	)

	REDIS_DB_PORT: int | None = Field(
		title="REDIS_DB_PORT", description="Port on which the Redis database is exposed.", default=None
	)

	REDIS_DB_NAME: int | None = Field(
		title="REDIS_DB_NAME", description="Name of the relational database.", default=None
	)

	# endregion

	# region NOSQL

	NOSQL_DB_HOST: str | None = Field()

	NOSQL_DB_PORT: int | None = Field()

	NOSQL_DB_USER: str | None = Field()

	NOSQL_DB_PASSWORD: str | None = Field()

	NOSQL_DB_NAME: str | None = Field()

	# endregion

	# region AI

	LLM_HOST: str | None = Field(title="LLM_HOST", description="Host on which the LLM is deployed.", default=None)

	LLM_PORT: str | None = Field(title="LLM_PORT", description="Port on which the LLM is exposed.", default=None)

	LLM_NAME: int | None = Field(title="LLM_NAME", description="Name of the LLM.", default=None)

	# endregion


SETTINGS = Settings(_env_file=".env", _env_file_encoding="utf-8")
