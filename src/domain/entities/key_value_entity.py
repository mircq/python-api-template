from pydantic import BaseModel, Field


class KeyValueEntity(BaseModel):
	""" """

	key: str = Field(
		title="key",
		description="Entity key",
	)

	value: str = Field(title="value", description="Entity value")
