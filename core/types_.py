from typing import Dict, TypeVar, Optional, Sequence

import typing as tp

from fastapi.params import Depends
from pydantic import BaseModel

from core.transformers._base import BaseTransformer
from core.validators._base import BaseValidator

PAGINATION = Dict[str, Optional[int]]
PYDANTIC_SCHEMA = BaseModel

T = TypeVar("T", bound=BaseModel)
DEPENDENCIES = Optional[Sequence[Depends]]

Transformer = BaseTransformer
TransformerClass = tp.Type[Transformer]

Validator = tp.TypeVar('Validator', bound=BaseValidator)
ValidatorClass = tp.Type[Validator]

_Transformer = tp.TypeVar('_Transformer', bound=BaseTransformer)
_TransformerClass = tp.Type[_Transformer]
_AnyTransformerClass = tp.Union[_TransformerClass, tp.List[_TransformerClass]]
