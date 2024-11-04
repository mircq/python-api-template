from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    port: int = Field(
        title="",
        description="",
        default=8000
    )

    relational_db_type: str | None = Field(
        title="",
        description="",
        default=None
    )

    relational_db_host: str | None = Field(
        title="",
        description="",
        default=None
    )

    relational_db_port: str | None = Field(
        title="",
        description="",
        default=None
    )

    relational_db_user: str | None = Field(
        title="",
        description="",
        default=None
    )

    relational_db_password: str | None = Field(
        title="",
        description="",
        default=None
    )


settings = Settings(_env_file='prod.env', _env_file_encoding='utf-8')

