from pydantic import UUID4

from src.application.interfaces.template_interface import ITemplateService
from src.domain.entities.patch_entity import PatchEntity
from src.domain.entities.template_entity import TemplateEntity
from src.domain.results.result import Result
from src.domain.utilities.exception_handler import exception_handler
from src.domain.utilities.logger import logger
from src.persistence.repositories.template_repository import TemplateRepository


class TemplateService(ITemplateService):
	"""
	Utility class to forward API request to the appropriate persistence/infrastructure function, as well as
	implementing some logic.
	"""

	# region POST
	@staticmethod
	@exception_handler
	async def post(entity: TemplateEntity) -> Result[TemplateEntity]:
		"""
		Create a new template.

		:param TemplateEntity entity: template to be created.
		:return: a Result object containing the created entity if operation has been successful, a Result object
		containing the error if the operation failed.
		:rtype: Result[TemplateEntity]
		"""

		logger.info(msg="Start")

		result: Result[TemplateEntity] = await TemplateRepository.post(entity=entity)

		logger.info(msg="End")

		return result

	# endregion

	# region GET
	@staticmethod
	@exception_handler
	async def get(id: UUID4) -> Result[TemplateEntity]:
		"""
		Retrieve a template from its id.

		:param UUID4 id: id of the template to be retrieved.
		:return: a Result object containing the retrieved entity if operation has been successful, a Result object
		containing the error if the operation failed.
		:rtype: Result[TemplateEntity]
		"""

		logger.info(msg="Start")

		result: Result[TemplateEntity] = await TemplateRepository.get(id=id)

		logger.info(msg="End")

		return result

	# endregion

	# region DELETE
	@staticmethod
	@exception_handler
	async def delete(id: UUID4) -> Result[TemplateEntity]:
		"""
		Delete a template from its id.

		:param UUID4 id: id of the template to be deleted.
		:return: a Result object containing the deleted entity if operation has been successful, a Result object
		containing the error if the operation failed.
		:rtype: Result[TemplateEntity]
		"""

		logger.info(msg="Start")

		result: Result[TemplateEntity] = await TemplateRepository.delete(id=id)

		logger.info(msg="End")

		return result

	# endregion

	# region PUT
	@staticmethod
	@exception_handler
	async def put(id: UUID4, entity: TemplateEntity) -> Result[TemplateEntity]:
		"""
		Update a template from its id and the given entity.

		:param UUID4 id: id of the template to be updated.
		:param TemplateEntity entity: entity with which the old entry will be overwritten.
		:return: a Result object containing the retrieved entity if operation has been successful, a Result object
		containing the error if the operation failed.
		:rtype: Result[TemplateEntity]
		"""

		logger.info(msg="Start")

		result: Result[TemplateEntity] = await TemplateRepository.put(id=id, entity=entity)

		logger.info(msg="End")

		return result

	# endregion

	# region PATCH
	@staticmethod
	@exception_handler
	async def patch(id: UUID4, patches: list[PatchEntity]) -> Result[TemplateEntity]:
		"""
		Patch a template from its id and the given entity.

		:param UUID4 id: id of the template to be updated.
		:param list[PatchEntity] patches: patches to be applied to the entry.
		:return: a Result object containing the retrieved entity if operation has been successful, a Result object
		containing the error if the operation failed.
		:rtype: Result[TemplateEntity]
		"""

		logger.info(msg="Start")

		result: Result[TemplateEntity] = await TemplateRepository.patch(id=id, patches=patches)

		logger.info(msg="End")

		return result

	# endregion
