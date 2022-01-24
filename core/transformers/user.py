from pydantic import Field

from core.transformers._base import BaseTransformer


class User(BaseTransformer):
    index: int
    name: str
    state: str
    position: str


class LoginTransformer(BaseTransformer):
    access_token: str = Field(description='本次登录的token')
    token_type: str = Field(default='Bearer', description='token的类型，统一为 Bearer')
    user_id: int


class GetMeTransformer(BaseTransformer):
    user_id: int
