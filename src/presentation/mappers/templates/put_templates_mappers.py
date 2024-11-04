from src.domain.entities.template_entity import TemplateEntity
from src.presentation.DTOs.templates.put_templates_input_dto import PutTemplateInputDTO
from src.presentation.DTOs.templates.put_templates_output_dto import PutTemplateOutputDTO


class PutTemplateMappers:

    """

    """

    @staticmethod
    def to_dto(entity: TemplateEntity) -> PutTemplateOutputDTO:
        """

        """

        return PutTemplateOutputDTO(**entity.model_dump())

    @staticmethod
    def to_entity(dto: PutTemplateInputDTO) -> TemplateEntity:
        """

        """

        return TemplateEntity(**dto.model_dump())

