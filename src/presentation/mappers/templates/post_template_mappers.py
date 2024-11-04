from src.domain.entities.template_entity import TemplateEntity
from src.presentation.DTOs.templates.post_templates_input_dto import PostTemplateOutputDTO, PostTemplateInputDTO


class PostTemplateMappers:

    """

    """

    @staticmethod
    def to_dto(entity: TemplateEntity) -> PostTemplateOutputDTO:
        """

        """

        return PostTemplateOutputDTO(**entity.model_dump())

    @staticmethod
    def to_entity(dto: PostTemplateInputDTO) -> TemplateEntity:
        """

        """

        return TemplateEntity(**dto.model_dump())

