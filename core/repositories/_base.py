import typing as tp

from core.models._base import BaseModel
from core.services import get_db
from core.validators._base import BaseValidator


class BaseRepository():
    pass


class CRUDRepository():
    pk: str = 'id'
    pk_type: tp.Type

    def __init__(self, Model: tp.Type[BaseModel]):
        self.Model = Model

        # self.pk = self.Model.__table__.primary_key.columns.keys()[0]

    def all(self, page_size: int = 15, page_to: int = 1):
        skip = (page_to - 1) * page_size
        db = next(get_db())
        data = db.query(self.Model).offset(skip).limit(page_size).all()

        return data

    def detail(self, id) -> BaseModel:
        db = next(get_db())
        data = db.query(self.Model).get(id)

        return data

    def create(self, payload: BaseValidator):
        db = next(get_db())
        model = self.Model(**payload.dict())
        db.add(model)
        db.commit()
        db.refresh(model)

        return model

    def partial_update(self, id, payload: BaseValidator):
        db = next(get_db())
        model = db.query(self.Model).get(id)

        for key, value in payload.dict(exclude={self.pk}).items():
            if hasattr(model, key):
                setattr(model, key, value)

        db.commit()
        db.refresh(model)

        return model

    def delete(self, id):
        db = next(get_db())
        model = db.query(self.Model).get(id)
        db.delete(model)

        return model


def register_action(resource_, path: str, method: str, doc: str):
    def wrapper(f):
        resource_.router.add_api_route(
            path,
            endpoint=f,
            methods=[method],
            name=doc
        )
    return wrapper
