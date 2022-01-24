import abc
import typing as tp

from fastapi import APIRouter

from core import types_ as tp_
from core.repositories._base import BaseRepository, CRUDRepository
from core.transformers._base import OrmTransformer
from core.types_ import ValidatorClass, Validator


class BaseAction(abc.ABC):
    method: str = 'POST'
    path: str = '/'

    Validator: tp.Optional[ValidatorClass] = None
    Transformer: tp.Optional[tp_._AnyTransformerClass] = None
    is_plural: bool = False

    handle: tp.Callable
    repository: tp.Union[BaseRepository, CRUDRepository]

    # pre_handle: Any = None
    # post_handle: Any = None
    # full_handle: Callable = None

    name_doc: tp.Optional[str] = None

    def __init__(
            self,
            repository: BaseRepository,
            Transformer: tp_._AnyTransformerClass,
            Validator: tp.Type[Validator] = None,
    ):
        self.repository = repository
        self.Validator = Validator
        self.Transformer = tp.List[Transformer] if self.is_plural else Transformer

        self.init_handle()

    @abc.abstractmethod
    def init_handle(self): pass  # noqa: E704 multiple statements on one line (def)

    def register_action(self, router: APIRouter):
        router.add_api_route(
            self.path,
            endpoint=self.handle,

            response_model=self.Transformer,
            methods=[self.method],
            name=self.name_doc,
        )


class SingleAction(BaseAction, abc.ABC):
    path = '/{id}'
    is_plural = False


class PluralAction(BaseAction, abc.ABC):
    path = '/'
    is_plural = True


class ListAction(PluralAction):
    is_plural = True
    method = 'GET'
    Transformer: tp.List[OrmTransformer]

    name_doc = '查看列表'

    def init_handle(self):
        self.handle = self.repository.all


class CreateAction(SingleAction):
    path = '/'
    method = 'POST'
    Transformer = OrmTransformer

    name_doc = '创建资源'

    def init_handle(self):
        def create(
                payload: self.Validator,  # type: ignore
        ):
            return self.repository.create(payload)

        self.handle = create


class DetailAction(SingleAction):
    method = 'GET'
    Transformer = OrmTransformer

    name_doc = '查看详情'

    def init_handle(self):
        self.handle = self.repository.detail


class PartialUpdateAction(SingleAction):
    method = 'PATCH'
    Transformer = OrmTransformer

    name_doc = '部分更新'

    def init_handle(self):
        def partial_update(
                id,
                payload: self.Validator,  # type: ignore
        ):
            return self.repository.partial_update(id, payload)

        self.handle = partial_update


class DeleteAction(SingleAction):
    method = 'DELETE'
    Transformer = OrmTransformer

    name_doc = '删除资源'

    def init_handle(self):
        self.handle = self.repository.delete
