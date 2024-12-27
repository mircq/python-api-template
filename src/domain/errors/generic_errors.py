from src.domain.errors.error import Error


class GenericErrors:
	@staticmethod
	def generic_error(details: str):
		return Error(
			message=f"A generic error occurred. Details: {details}",
			status_code=500,
		)

	@staticmethod
	def not_found_error(key: str, type: str | None = None):
		return Error(
			message=f"Entry of type {type} with key={key} does not exist."
			if type
			else f"Entry with key={key} does not exist.",
			status_code=404,
		)
