
from core.actions.user import UserAction, LoginAction, GetMeAction
from core.repositories.user import UserRepository
from core.resources._base import BaseResource
from core.transformers.user import User as Transformer


class UserResource(BaseResource):
    name = 'user'
    name_doc = ''
    path = '/users'

    Actions = [UserAction, LoginAction, GetMeAction]

    repository = UserRepository()
    Transformer = Transformer

    # create_Validator = Validator1
    # partial_update_Validator = Validator2


resource = UserResource().register_resource()
