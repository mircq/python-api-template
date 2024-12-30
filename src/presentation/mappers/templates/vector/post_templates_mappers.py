from src.domain.entities.vector_database_template_entity import VectorDatabaseTemplateEntity
from src.presentation.DTOs.templates.vector.post_templates_output_dto import PostTemplateOutputDTO


class PostTemplateMappers:
	""" """

	@staticmethod
	def to_dto(entity: VectorDatabaseTemplateEntity) -> PostTemplateOutputDTO:
		""" """

		return PostTemplateOutputDTO(**entity.model_dump())
