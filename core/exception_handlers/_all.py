import typing as tp

from fastapi import FastAPI, Query, Request, Depends, Header
from fastapi.responses import JSONResponse, PlainTextResponse, StreamingResponse
from fastapi.exceptions import RequestValidationError, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException

from core.exceptions._all import MyHTTPException


def err(code: int, msg: str, details: tp.Any = None):
    return {
        "code": code,
        "msg": msg,
        "details": details
    }


async def handle_validation_exception(request, exc: RequestValidationError):
    return JSONResponse(
        status_code=200,
        content=err(400, '参数错误', exc.errors()),
    )


async def handle_http_exception(request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=200,
        content=err(exc.status_code, '非法请求', str(exc.detail)),
    )


async def handle_my_http_exception(request, exc: MyHTTPException):
    return JSONResponse(
        status_code=200,
        content=err(exc.status_code, '非法请求', str(exc.detail)),
    )


async def handle_exception(request: Request, exc: Exception):
    print(type(exc))
    return JSONResponse(
        status_code=200,
        content=err(400, '系统错误', str(exc)),
    )
