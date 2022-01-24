from starlette.exceptions import HTTPException
import typing as tp


class MyHTTPException(HTTPException):
    title: str

    def __init__(self, title, detail: tp.Any = None, status_code: int = 4000) -> None:
        if detail is None:
            detail = ''
        super().__init__(status_code, detail)
        self.title = title


class NormalException(MyHTTPException): pass


class TokenVerifyException(MyHTTPException):
    def __init__(self, title, detail: tp.Any = None, status_code: int = 4001) -> None:
        super().__init__(title, detail, status_code)
