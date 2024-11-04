from src.domain.entities.template_entity import TemplateEntity
from src.presentation.DTOs.templates.get_templates_output_dto import GetTemplateOutputDTO


class GetTemplateMappers:

    """

    """

    @staticmethod
    def to_dto(entity: TemplateEntity) -> GetTemplateOutputDTO:
        """

        """

        return GetTemplateOutputDTO(**entity.model_dump())