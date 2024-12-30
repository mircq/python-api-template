from src.domain.entities.patch_entity import PatchEntity
from src.presentation.DTOs.generic.patch_dto import PatchDTO


class PatchMappers:
	""" """

	@staticmethod
	def to_entity(dto: PatchDTO) -> PatchEntity:
		""" """

		return PatchEntity(**dto.model_dump())
