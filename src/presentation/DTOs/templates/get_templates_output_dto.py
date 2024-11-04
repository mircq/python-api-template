from pydantic import UUID4, BaseModel, Field


class GetTemplateOutputDTO(BaseModel):

    id: UUID4 = Field(
        title="id",
        description="Entity id"
    )

    description: str = Field(
        title="description",
        description="Entity description"
    )