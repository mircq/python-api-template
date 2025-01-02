from src.domain.entities.template_entity import TemplateEntity
from src.domain.utilities.logger import logger
from src.presentation.DTOs.templates.nosql.put_templates_input_dto import PutTemplateInputDTO
from src.presentation.DTOs.templates.nosql.put_templates_output_dto import PutTemplateOutputDTO


class PutTemplateMappers:
	""" """

	@staticmethod
	def to_dto(entity: TemplateEntity) -> PutTemplateOutputDTO:
		""" """
		logger.info(msg="Start")
		logger.debug(msg=f"Input params: entity={entity}")
		dto: PutTemplateOutputDTO = PutTemplateOutputDTO(**entity.model_dump())

		logger.info(msg="End")
		logger.debug(msg=f"Return value={dto}")

		return dto

	@staticmethod
	def to_entity(dto: PutTemplateInputDTO) -> TemplateEntity:
		""" """

		logger.info(msg="Start")
		logger.debug(msg=f"Input params: dto={dto}")

		entity: TemplateEntity = TemplateEntity(**dto.model_dump())

		logger.info(msg="End")
		logger.debug(msg=f"Return value={entity}")

		return entity
