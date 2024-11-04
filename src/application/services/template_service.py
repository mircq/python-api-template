from pydantic import UUID4

from src.application.interfaces.template_interface import ITemplateService
from src.domain.entities.template_entity import TemplateEntity
from src.domain.results.result import Result
from src.persistence.repositories.template_repository import TemplateRepository


class TemplateService(ITemplateService):

    """

    """

    #region POST

    async def post(self, entity: TemplateEntity) -> Result[TemplateEntity]:
        """

        """

        result: Result[TemplateEntity] = await TemplateRepository().post(entity=entity)

        return result

    #endregion

    #region GET

    async def get(self, id: UUID4) -> Result[TemplateEntity]:
        """

        """

        result: Result[TemplateEntity] = await TemplateRepository().get(id=id)

        return result

    #endregion

    #region DELETE

    async def delete(self, id: UUID4) -> Result[TemplateEntity]:
        """

        """

        result: Result[TemplateEntity] = await TemplateRepository().delete(id=id)

        return result

    #endregion

    # region DELETE

    async def put(self, id: UUID4, entity: TemplateEntity) -> Result[TemplateEntity]:
        """

        """

        result: Result[TemplateEntity] = await TemplateRepository().put(id=id, entity=entity)

        return result

    # endregion
