from src.domain.entities.vector_database_template_entity import VectorDatabaseTemplateEntity
from src.presentation.DTOs.templates.vector.delete_templates_output_dto import DeleteTemplateOutputDTO


class DeleteTemplateMappers:
	""" """

	@staticmethod
	def to_dto(entity: VectorDatabaseTemplateEntity) -> DeleteTemplateOutputDTO:
		""" """

		return DeleteTemplateOutputDTO(**entity.model_dump())
