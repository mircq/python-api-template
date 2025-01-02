from src.domain.entities.template_entity import TemplateEntity
from src.domain.utilities.logger import logger
from src.presentation.DTOs.templates.sql.get_templates_output_dto import GetTemplateOutputDTO


class GetTemplateMappers:
	""" """

	@staticmethod
	def to_dto(entity: TemplateEntity) -> GetTemplateOutputDTO:
		""" """

		logger.info(msg="Start")
		logger.debug(msg=f"Input params: entity={entity}")
		dto: GetTemplateOutputDTO = GetTemplateOutputDTO(**entity.model_dump())
		logger.info(msg="End")
		logger.debug(msg=f"Return value={dto}")
		return dto
