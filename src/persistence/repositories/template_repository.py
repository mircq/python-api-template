from pydantic import UUID4
# TODO check sqlalchemy dependency
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from src.domain.entities.template_entity import TemplateEntity
from src.domain.results.result import Result
from src.domain.utilities.settings import settings
from src.persistence.objects.template import Template


class TemplateRepository:

    def __init__(self):

        url = f"{settings.relational_db_type}://{settings.relational_db_user}:{settings.relational_db_password}@{settings.relational_db_host}:{settings.relational_db_port}"

        engine = create_async_engine(url=url)

        self.session = AsyncSession(engine)

    #region POST

    async def post(self, entity: TemplateEntity) -> Result[TemplateEntity]:

        """

        :param TemplateEntity entity:
        :return:
        """

        #TODO check if this mapping can be avoided, or add a mapper instead
        t: Template = Template(**entity.model_dump())

        self.session.add(instance=t)
        await self.session.commit()
        await self.session.refresh(t)

        return Result.ok(value=t)

    #endregion

    #region GET

    async def get(self, id: UUID4) -> Result[TemplateEntity]:

        """

        :param UUID4 id:
        :return:
        """

        statement = select(Template).where(Template.id == id)

        entity = self.session.exec(statement).first()

        return Result.ok(value=entity)

    #endregion

    # region DELETE

    async def delete(self, id: UUID4) -> Result[TemplateEntity]:
        """

        :param UUID4 id:
        :return:
        """

        statement = select(Template).where(Template.id == id)

        results = self.session.exec(statement)

        template = results.one()

        await self.session.delete(template)
        await self.session.commit()

        return Result.ok(value=template)

    # endregion

    #region UPDATE

    async def put(self, id: UUID4, entity: TemplateEntity) -> Result[TemplateEntity]:
        """

        :param UUID4 id:
        :return:
        """

        statement = select(Template).where(Template.id == id)
        results = self.session.exec(statement)
        template = results.one()

        # TODO is there a way to do it dynamically?
        template.description = entity.description
        self.session.add(template)
        await self.session.commit()
        await self.session.refresh(template)

        return Result.ok(value=template)

    #endregion