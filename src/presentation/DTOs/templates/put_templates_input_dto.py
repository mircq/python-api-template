from pydantic import BaseModel, Field


class PutTemplateInputDTO(BaseModel):
	description: str = Field(title="description", description="Entity description")
