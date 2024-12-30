from src.domain.entities.template_entity import TemplateEntity
from src.presentation.DTOs.templates.patch_templates_output_dto import PatchTemplateOutputDTO


class PatchTemplateMappers:
	""" """

	@staticmethod
	def to_dto(entity: TemplateEntity) -> PatchTemplateOutputDTO:
		""" """

		return PatchTemplateOutputDTO(**entity.model_dump())
