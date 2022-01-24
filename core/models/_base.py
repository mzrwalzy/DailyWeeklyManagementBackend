from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from core.utils import camel2snake


@as_declarative()
class BaseModel:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return camel2snake(cls.__name__)

    def to_dict(self):
        return {k: self.__dict__[k] for k in self.__dict__ if not k.startswith('_')}
