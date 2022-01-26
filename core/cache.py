# -*- coding:utf-8 -*-
# @Time     : 2022/1/24 9:44
# @Author   : Charon.
import json
import typing as tp

from core.services import redis_client


class Cache:
    DEFAULT_EXPIRATION: int = 86400

    def __init__(self):
        self.redis = redis_client

    def get(self, name, add_ex: bool = True) -> tuple[bool, tp.Any]:
        v = self.redis.get(name)
        if add_ex:
            self.redis.expire(name, self.DEFAULT_EXPIRATION)
        try:
            v = json.loads(v)
        finally:
            return v is not None, v

    def set(self, key: str, value: tp.Any, ex: int = None):
        if ex is None:
            ex = self.DEFAULT_EXPIRATION
        if isinstance(value, dict):
            value = json.dumps(value)
        return self.redis.set(key, value, ex=ex)


cache = Cache()
