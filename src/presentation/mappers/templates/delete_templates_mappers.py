from src.domain.entities.template_entity import TemplateEntity
from src.presentation.DTOs.templates.delete_templates_output_dto import DeleteTemplateOutputDTO


class DeleteTemplateMappers:

    """

    """

    @staticmethod
    def to_dto(entity: TemplateEntity) -> DeleteTemplateOutputDTO:
        """

        """

        return DeleteTemplateOutputDTO(**entity.model_dump())