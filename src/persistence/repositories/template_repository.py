from src.domain.entities.template_entity import TemplateEntity
from src.domain.results.result import Result


class TemplateRepository:

    def post(self, entity: TemplateEntity) -> Result[TemplateEntity]:

        """

        :param TemplateEntity entity:
        :return:
        """

        session.add(entity)
        session.commit()
        session.refresh(hero)

        return Result.ok(value=entity)