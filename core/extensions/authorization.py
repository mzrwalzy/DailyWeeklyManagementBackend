# -*- coding:utf-8 -*-
# @Time     : 2022/1/24 9:10
# @Author   : Charon.
import typing as tp
from datetime import datetime, timedelta

import arrow
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseSettings
from sqlalchemy.orm import Session
from starlette.requests import Request

from core.cache import cache
from core.configs import db as DB
from core.exceptions._all import TokenVerifyException
from core.models.report import Employee
from core.services import get_db


class UserTokenConfig(BaseSettings):
    """对用户登录时处理token的相关配置"""
    # 通过命令行 `openssl rand -hex 32` 可以生成该安全密钥
    SECRET_KEY: str = "4650c5883b44053fdf706eb7a2c40f99ff9b91fbe5436f95abada8e01f2e3673"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = DB.ACCESS_TOKEN_EXPIRE_MINUTES


user_token_conf = UserTokenConfig()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_pwd_hash(pwd):
    return pwd_context.hash(pwd)


def authenticate_user(user: Employee, password: str) -> tp.Union[bool, Employee]:
    """
    验证用户合法性
    :return: 若验证成功则返回 User 对象；若验证失败则返回 False
    """

    if not user:
        return False
    hashed_password = user.password
    if not pwd_context.verify(password, hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, user_token_conf.SECRET_KEY, algorithm=user_token_conf.ALGORITHM)
    return encoded_jwt


async def fetch_token(request: Request) -> tp.Optional[str]:
    """
    在 request 中获取到 oauth2 认证所需要的信息
    :return: 取出的 token
    """
    try:
        token = await oauth2_scheme(request)
    except HTTPException as e:
        raise TokenVerifyException(e.detail)
    return token


def verify_token(token: str):
    """
    根据请求头部的 Authorization 字段，在 Redis 进行验证并获取用户的 username
    :return: 验证成功时返回用户的 username，验证失败则抛出异常
    :raise: TokenVerifyException 验证失败时抛出此异常
    """
    # 验证 token 是否为空
    if token is None:
        raise TokenVerifyException('token验证失败')
    # 查询 redis_db 进行验证
    ok, user_id = cache.get(token)
    if not ok and user_id is None:
        raise TokenVerifyException('token验证失败')
    return user_id
