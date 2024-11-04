
from fastapi import APIRouter, HTTPException, Body, Path
from pydantic import UUID4

from src.application.services.template_service import TemplateService
from src.domain.entities.template_entity import TemplateEntity
from src.domain.results.result import Result
from src.presentation.DTOs.templates.delete_templates_output_dto import DeleteTemplateOutputDTO
from src.presentation.DTOs.templates.get_templates_output_dto import GetTemplateOutputDTO
from src.presentation.DTOs.templates.post_templates_input_dto import PostTemplateInputDTO, PostTemplateOutputDTO
from src.presentation.DTOs.templates.put_templates_input_dto import PutTemplateInputDTO
from src.presentation.DTOs.templates.put_templates_output_dto import PutTemplateOutputDTO
from src.presentation.examples.templates.delete_templates_request_examples import DELETE_TEMPLATES_PATH_EXAMPLE
from src.presentation.examples.templates.delete_templates_response_examples import DELETE_TEMPLATES_RESPONSE_EXAMPLES
from src.presentation.examples.templates.get_templates_request_examples import GET_TEMPLATES_PATH_EXAMPLE
from src.presentation.examples.templates.get_templates_response_examples import GET_TEMPLATES_RESPONSE_EXAMPLES
from src.presentation.examples.templates.post_templates_request_examples import POST_TEMPLATES_BODY_EXAMPLES
from src.presentation.examples.templates.post_templates_response_examples import POST_TEMPLATES_RESPONSE_EXAMPLES
from src.presentation.examples.templates.put_templates_request_examples import PUT_TEMPLATES_PATH_EXAMPLE, \
    PUT_TEMPLATES_BODY_EXAMPLES
from src.presentation.examples.templates.put_templates_response_examples import PUT_TEMPLATES_RESPONSE_EXAMPLES

from src.presentation.mappers.templates.delete_templates_mappers import DeleteTemplateMappers
from src.presentation.mappers.templates.get_templates_mappers import GetTemplateMappers
from src.presentation.mappers.templates.post_template_mappers import PostTemplateMappers
from src.presentation.mappers.templates.put_templates_mappers import PutTemplateMappers

template_router = APIRouter(
    prefix="/templates",
    tags=["Template"]
)

#region POST
@template_router.post(
    path="/",
    summary="Create a new template.",
    description="Create a new template.",
    status_code=201,
    responses=POST_TEMPLATES_RESPONSE_EXAMPLES
)
async def create_template(
        dto: PostTemplateInputDTO = Body(examples=POST_TEMPLATES_BODY_EXAMPLES)
) -> PostTemplateOutputDTO:

    """

    :param dto:
    :return:
    """

    entity: TemplateEntity = PostTemplateMappers.to_entity(dto=dto)

    result: Result[TemplateEntity] = await TemplateService().post(entity=entity)

    if result.failed:

        raise HTTPException(detail=result.error.message, status_code=result.error.status_code)

    output: PostTemplateOutputDTO = PostTemplateMappers.to_dto(entity=result.value)

    return output
#endregion

#region GET
@template_router.get(
    path="/{id}",
    summary="Get a template.",
    description="Retrieve a template from its id.",
    responses=GET_TEMPLATES_RESPONSE_EXAMPLES
)
async def get_template(
        id: UUID4 = Path(example=GET_TEMPLATES_PATH_EXAMPLE)
) -> GetTemplateOutputDTO:

    """

    :param UUID4 id:
    :return:
    """


    result: Result[TemplateEntity] = await TemplateService().get(id=id)

    if result.failed:

        raise HTTPException(detail=result.error.message, status_code=result.error.status_code)

    output: GetTemplateOutputDTO = GetTemplateMappers.to_dto(entity=result.value)

    return output
#endregion

#region DELETE
@template_router.delete(
    path="/{id}",
    summary="Delete a template.",
    description="Delete a template with the given id.",
    responses=DELETE_TEMPLATES_RESPONSE_EXAMPLES
)
async def delete_template(
        id: UUID4 = Path(example=DELETE_TEMPLATES_PATH_EXAMPLE)
) -> DeleteTemplateOutputDTO:

    """

    :param UUID4 id:
    :return:
    """


    result: Result[TemplateEntity] = await TemplateService().delete(id=id)

    if result.failed:

        raise HTTPException(detail=result.error.message, status_code=result.error.status_code)

    output: DeleteTemplateOutputDTO = DeleteTemplateMappers.to_dto(entity=result.value)

    return output
#endregion

#region UPDATE
@template_router.put(
    path="/{id}",
    summary="Update a template.",
    description="Update the template with the given id.",
    responses=PUT_TEMPLATES_RESPONSE_EXAMPLES
)
async def put_template(
        id: UUID4 = Path(example=PUT_TEMPLATES_PATH_EXAMPLE),
        dto: PutTemplateInputDTO = Body(examples=PUT_TEMPLATES_BODY_EXAMPLES)
) -> PutTemplateOutputDTO:

    """

    :param UUID4 id:
    :return:
    """

    entity: TemplateEntity = PutTemplateMappers.to_entity(dto=dto)

    result: Result[TemplateEntity] = await TemplateService().put(id=id, entity=entity)

    if result.failed:

        raise HTTPException(detail=result.error.message, status_code=result.error.status_code)

    output: PutTemplateOutputDTO = PutTemplateMappers.to_dto(entity=result.value)

    return output
#endregion