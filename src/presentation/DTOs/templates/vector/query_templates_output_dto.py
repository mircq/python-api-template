from pydantic import BaseModel, Field, UUID4

from src.presentation.DTOs.templates.vector.template_payload_dto import TemplatePayloadDTO


class QueryTemplateOutputDTO(BaseModel):
	"""Represents the output DTO returned after querying the templates collection."""

	id: UUID4 = Field(title="id", description="Id of the point into the Vector database collection.")

	vector: list[float] = Field(title="vector", description="Vector associated to the point.")

	payload: TemplatePayloadDTO = Field(title="payload", description="Template payload.")
