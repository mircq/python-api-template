from src.domain.entities.template_entity import TemplateEntity
from src.presentation.DTOs.template_DTOs import PostTemplateInputDTO, PostTemplateOutputDTO


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