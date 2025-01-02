from src.domain.entities.template_entity import TemplateEntity
from src.domain.utilities.logger import logger
from src.presentation.DTOs.templates.nosql.post_templates_input_dto import PostTemplateInputDTO
from src.presentation.DTOs.templates.nosql.post_templates_output_dto import PostTemplateOutputDTO


class PostTemplateMappers:
	""" """

	@staticmethod
	def to_dto(entity: TemplateEntity) -> PostTemplateOutputDTO:
		""" """
		logger.info(msg="Start")
		logger.debug(msg=f"Input params: entity={entity}")
		dto: PostTemplateOutputDTO = PostTemplateOutputDTO(**entity.model_dump())

		logger.info(msg="End")
		logger.debug(msg=f"Return value={dto}")

		return dto

	@staticmethod
	def to_entity(dto: PostTemplateInputDTO) -> TemplateEntity:
		""" """

		logger.info(msg="Start")
		logger.debug(msg=f"Input params: dto={dto}")

		entity: TemplateEntity = TemplateEntity(**dto.model_dump())

		logger.info(msg="End")
		logger.debug(msg=f"Return value={entity}")

		return entity
