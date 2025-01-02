from src.domain.entities.vector_database_template_entity import VectorDatabaseTemplateEntity
from src.domain.utilities.logger import logger
from src.presentation.DTOs.templates.vector.query_templates_output_dto import QueryTemplateOutputDTO


class QueryTemplateMappers:
	""" """

	@staticmethod
	def to_dto(entity: VectorDatabaseTemplateEntity) -> QueryTemplateOutputDTO:
		""" """

		logger.info(msg="Start")
		logger.debug(msg=f"Input params: entity={entity}")

		dto: QueryTemplateOutputDTO = QueryTemplateOutputDTO(**entity.model_dump())

		logger.info(msg="End")
		logger.debug(msg=f"Return value={dto}")

		return dto
