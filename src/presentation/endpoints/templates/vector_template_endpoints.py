from fastapi import APIRouter, HTTPException, Body, Path
from pydantic import UUID4

from src.application.services.vector_template_service import VectorTemplateService
from src.domain.entities.vector_database_template_entity import VectorDatabaseTemplateEntity
from src.domain.results.result import Result
from src.domain.utilities.logger import logger
from src.presentation.DTOs.templates.vector.delete_templates_output_dto import DeleteTemplateOutputDTO
from src.presentation.DTOs.templates.vector.post_templates_input_dto import PostTemplateInputDTO
from src.presentation.DTOs.templates.vector.post_templates_output_dto import PostTemplateOutputDTO
from src.presentation.DTOs.templates.vector.query_templates_input_dto import QueryTemplateInputDTO
from src.presentation.DTOs.templates.vector.query_templates_output_dto import QueryTemplateOutputDTO
from src.presentation.examples.templates.vector.delete_templates_request_examples import DELETE_TEMPLATES_PATH_EXAMPLE
from src.presentation.examples.templates.vector.delete_templates_response_examples import (
	DELETE_TEMPLATES_RESPONSE_EXAMPLES,
)
from src.presentation.examples.templates.vector.post_templates_request_examples import POST_TEMPLATES_BODY_EXAMPLES
from src.presentation.examples.templates.vector.post_templates_response_examples import POST_TEMPLATES_RESPONSE_EXAMPLES
from src.presentation.examples.templates.vector.query_templates_request_examples import QUERY_TEMPLATES_BODY_EXAMPLES
from src.presentation.examples.templates.vector.query_templates_response_examples import (
	QUERY_TEMPLATES_RESPONSE_EXAMPLES,
)
from src.presentation.mappers.templates.vector.delete_templates_mappers import DeleteTemplateMappers
from src.presentation.mappers.templates.vector.post_templates_mappers import PostTemplateMappers
from src.presentation.mappers.templates.vector.query_templates_mappers import QueryTemplateMappers

vector_template_router = APIRouter(prefix="/vector/templates", tags=["Vector"])


# region POST
@vector_template_router.post(
	path="/",
	summary="Create a new template.",
	description="Create a new template.",
	status_code=201,
	responses=POST_TEMPLATES_RESPONSE_EXAMPLES,
)
async def create_template(
	dto: PostTemplateInputDTO = Body(examples=POST_TEMPLATES_BODY_EXAMPLES),
) -> list[PostTemplateOutputDTO]:
	"""

	:param dto:
	:return:
	"""

	logger.info(msg="Calling POST /vector/templates")

	result: Result[list[VectorDatabaseTemplateEntity]] = await VectorTemplateService.post(text=dto.text)

	if result.failed:
		raise HTTPException(detail=result.error.message, status_code=result.error.status_code)

	output: list[PostTemplateOutputDTO] = [PostTemplateMappers.to_dto(entity=entity) for entity in result.value]

	logger.info(msg="Successfully returning from POST /vector/templates")

	return output


@vector_template_router.post(
	path="/query",
	summary="Query a template.",
	description="Perform a query on the 'templates' Vector database collection.",
	responses=QUERY_TEMPLATES_RESPONSE_EXAMPLES,
)
async def query_template(
	dto: QueryTemplateInputDTO = Body(examples=QUERY_TEMPLATES_BODY_EXAMPLES),
) -> list[QueryTemplateOutputDTO]:
	"""

	:param QueryTemplateInputDTO dto:
	:return:
	"""

	result: Result[list[VectorDatabaseTemplateEntity]] = await VectorTemplateService.query(text=dto.text)

	if result.failed:
		raise HTTPException(detail=result.error.message, status_code=result.error.status_code)

	output: list[QueryTemplateOutputDTO] = [QueryTemplateMappers.to_dto(entity=entity) for entity in result.value]

	return output


# endregion


# region DELETE
@vector_template_router.delete(
	path="/{id}",
	summary="Delete a template.",
	description="Delete a template with the given id.",
	responses=DELETE_TEMPLATES_RESPONSE_EXAMPLES,
)
async def delete_template(id: UUID4 = Path(example=DELETE_TEMPLATES_PATH_EXAMPLE)) -> DeleteTemplateOutputDTO:
	"""

	:param UUID4 id:
	:return:
	"""

	result: Result[VectorDatabaseTemplateEntity] = await VectorTemplateService.delete(id=id)

	if result.failed:
		raise HTTPException(detail=result.error.message, status_code=result.error.status_code)

	output: DeleteTemplateOutputDTO = DeleteTemplateMappers.to_dto(entity=result.value)

	return output


# endregion
