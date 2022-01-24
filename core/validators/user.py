
import typing as tp
from core.validators._base import BaseValidator


class UserValidator(BaseValidator):
    pass


class LoginValidator(BaseValidator):
    username: str
    password: str
