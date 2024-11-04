from abc import abstractmethod, ABC

from src.domain.entities.template_entity import TemplateEntity


class TemplateInterface(ABC):

    @abstractmethod
    def post(self, entity: TemplateEntity) -> TemplateEntity:
        ...

