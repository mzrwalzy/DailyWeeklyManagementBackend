from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException

from core.exception_handlers import _all as exception_handlers
from core.exceptions import _all as exceptions


def register_exception_handlers(app: FastAPI):
    for exception_class, exception_handler in [
        (RequestValidationError, exception_handlers.handle_validation_exception),
        (exceptions.MyHTTPException, exception_handlers.handle_my_http_exception),
        (StarletteHTTPException, exception_handlers.handle_http_exception),
        (Exception, exception_handlers.handle_exception)
    ]:
        app.add_exception_handler(exception_class, exception_handler)

