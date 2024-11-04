
from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from src.application.services.template_service import TemplateService
from src.domain.entities.template_entity import TemplateEntity
from src.domain.results.result import Result
from src.presentation.DTOs.template_DTOs import PostTemplateInputDTO, PostTemplateOutputDTO
from src.presentation.mappers.template_mappers import PostTemplateMappers

template_router = APIRouter(
    prefix="/templates",
    tags=["Template"]
)

@template_router.post(
    path="/",
    summary="Create a new template.",
    description="Create a new template."
)
async def create_hero(dto: PostTemplateInputDTO, session: SessionDep) -> PostTemplateOutputDTO:

    entity: TemplateEntity = PostTemplateMappers.to_entity(dto=dto)

    result: Result[TemplateEntity] = await TemplateService().post(entity=entity)

    if result.failed:

        raise HTTPException(detail=result.error.message, status_code=result.error.status_code)

    output: PostTemplateOutputDTO = PostTemplateMappers.to_dto(entity=result.value)

    return output