from src.domain.entities.template_entity import TemplateEntity
from src.domain.utilities.logger import logger
from src.presentation.DTOs.templates.sql.patch_templates_output_dto import PatchTemplateOutputDTO


class PatchTemplateMappers:
	""" """

	@staticmethod
	def to_dto(entity: TemplateEntity) -> PatchTemplateOutputDTO:
		""" """

		logger.info(msg="Start")
		logger.debug(msg=f"Input params: entity={entity}")

		dto: PatchTemplateOutputDTO = PatchTemplateOutputDTO(**entity.model_dump())

		logger.info(msg="End")
		logger.debug(msg=f"Return value={dto}")

		return dto
