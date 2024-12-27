from src.domain.entities.template_entity import TemplateEntity
from beanie import Document


class NoSQLTemplate(TemplateEntity, Document):
	class Settings:
		name = "templates"
