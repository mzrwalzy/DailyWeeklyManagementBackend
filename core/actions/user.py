from core.actions._base import SingleAction, ListAction
from core.transformers.user import LoginTransformer, GetMeTransformer


class UserAction(ListAction):
    path = '/'

    def init_handle(self):
        self.handle = self.repository.all


class LoginAction(SingleAction):
    path = '/login'
    method = 'POST'
    Transformer = LoginTransformer

    def init_handle(self):
        self.handle = self.repository.login


class GetMeAction(SingleAction):
    path = '/me'
    method = 'GET'

    def init_handle(self):
        self.handle = self.repository.get_me
