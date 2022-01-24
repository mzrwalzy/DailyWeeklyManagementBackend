import typing as tp

from fastapi import APIRouter

from core.actions._base import BaseAction
from core.repositories._base import BaseRepository
from core.transformers._base import BaseTransformer


class BaseResource:
    name: str
    name_doc: str
    path: str
    router: APIRouter = APIRouter()
    Actions: tp.List[tp.Type[BaseAction]] = []

    repository: BaseRepository
    Transformer: tp.Type[BaseTransformer]

    def __init__(self):
        self.router: APIRouter = APIRouter(prefix=self.path, tags=[self.name_doc])

    def register_resource(self):
        for Action in self.Actions:
            _Transformer = Action.Transformer if Action.Transformer is not None else self.Transformer
            Action(self.repository, _Transformer).register_action(self.router)
        return self

