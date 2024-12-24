from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PORT: int = Field(title="PORT", description="Port on which the microservice is exposed.", default=8000)

    LOG_LEVEL: Literal["debug", "info", "warning", "error"] = Field(
        title="LOG_LEVEL", description="Level for log display.", default="info"
    )

    RELATIONAL_DB_TYPE: str = Field(title="RELATIONAL_DB_TYPE", description="Type of relational database used.")

    RELATIONAL_DB_HOST: str = Field(
        title="RELATIONAL_DB_HOST", description="Host on which the relational database is deployed."
    )

    RELATIONAL_DB_PORT: str = Field(
        title="RELATIONAL_DB_PORT", description="Port on which the relational database is exposed."
    )

    RELATIONAL_DB_USER: str = Field(
        title="RELATIONAL_DB_USER", description="Username for accessing relational database."
    )

    RELATIONAL_DB_PASSWORD: str = Field(
        title="RELATIONAL_DB_PASSWORD", description="Password for accessing relational database."
    )

    RELATIONAL_DB_NAME: str | None = Field(title="RELATIONAL_DB_NAME", description="Name of the relational database.")


    REDIS_DB_HOST: str | None = Field()

    REDIS_DB_USER: str | None = Field()

    REDIS_DB_PASSWORD: str | None = Field()

    REDIS_DB_PORT: int | None = Field()

    REDIS_DB_NAME: int | None = Field()


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')

