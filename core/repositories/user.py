import typing as tp

from fastapi import Depends, Header
from fastapi.security import OAuth2PasswordRequestForm
from requests import request

from core.cache import cache
from core.configs import db as DB
from core.exceptions._all import TokenVerifyException, NormalException
from core.extensions.authorization import authenticate_user, create_access_token, fetch_token, oauth2_scheme, \
    verify_token
from core.models.user import UserEmployee, UserDailyPlan, Position, Condition
from core.repositories._base import BaseRepository
from core.services import get_db
from core.validators.user import LoginValidator


class UserRepository(BaseRepository):
    def all(self) -> tp.Any:
        db_client = get_db()
        db = next(db_client)
        res = (db.query(UserEmployee.id, UserEmployee.name, Condition.condition, Position.position)
               .filter(UserEmployee.id == UserDailyPlan.id, UserEmployee.position == Position.id,
                       UserEmployee.today_condition == Condition.id).all())

        def handle_res(x):
            return {
                'index': x[0],
                'name': x[1],
                'position': x[3],
                'state': x[2]
            }

        res = list(map(lambda x: handle_res(x), res))

        return res

    def login(self, payload: OAuth2PasswordRequestForm = Depends()):
        db_client = get_db()
        db = next(db_client)
        username = payload.username
        password = payload.password

        user = db.query(UserEmployee).filter(UserEmployee.username == username).first()
        user = authenticate_user(user, password)
        if not user:
            raise NormalException('没有该用户')
        token_expire = int(DB.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token({"username": user.username}, token_expire)

        cache.set(access_token, user.id, ex=token_expire * 60)
        return {'access_token': access_token, 'token_type': 'Bearer', 'user_id': user.id}

    def get_me(self, token: str = Header(None)):
        user_id = verify_token(token)
        db_client = get_db()
        db = next(db_client)

        result = (db.query(UserEmployee.id, UserEmployee.name, Condition.condition, Position.position)
                  .filter(UserEmployee.id == user_id, UserEmployee.position == Position.id,
                          UserEmployee.today_condition == Condition.id).first())

        if not result:
            cache.redis.delete(token)
            raise NormalException('没有该用户')

        res = {
            'index': result[0],
            'name': result[1],
            'position': result[3],
            'state': result[2]
        }

        return res
