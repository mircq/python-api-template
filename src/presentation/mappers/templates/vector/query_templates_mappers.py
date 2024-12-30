from src.domain.entities.vector_database_template_entity import VectorDatabaseTemplateEntity
from src.presentation.DTOs.templates.vector.query_templates_output_dto import QueryTemplateOutputDTO


class QueryTemplateMappers:
	""" """

	@staticmethod
	def to_dto(entity: VectorDatabaseTemplateEntity) -> QueryTemplateOutputDTO:
		""" """

		return QueryTemplateOutputDTO(**entity.model_dump())
