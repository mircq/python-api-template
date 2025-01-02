from src.domain.entities.vector_database_template_entity import VectorDatabaseTemplateEntity
from src.domain.utilities.logger import logger
from src.presentation.DTOs.templates.vector.post_templates_output_dto import PostTemplateOutputDTO


class PostTemplateMappers:
	""" """

	@staticmethod
	def to_dto(entity: VectorDatabaseTemplateEntity) -> PostTemplateOutputDTO:
		""" """

		logger.info(msg="Start")
		logger.debug(msg=f"Input params: entity={entity}")

		dto: PostTemplateOutputDTO = PostTemplateOutputDTO(**entity.model_dump())

		logger.info(msg="End")
		logger.debug(msg=f"Return value={dto}")

		return dto
