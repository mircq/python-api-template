from src.domain.entities.template_entity import TemplateEntity
from src.domain.utilities.logger import logger
from src.presentation.DTOs.templates.sql.delete_templates_output_dto import DeleteTemplateOutputDTO


class DeleteTemplateMappers:
	""" """

	@staticmethod
	def to_dto(entity: TemplateEntity) -> DeleteTemplateOutputDTO:
		""" """

		logger.info(msg="Start")
		logger.debug(msg=f"Input params: entity={entity}")
		dto: DeleteTemplateOutputDTO = DeleteTemplateOutputDTO(**entity.model_dump())
		logger.info(msg="End")
		logger.debug(msg=f"Return value={dto}")

		return dto
