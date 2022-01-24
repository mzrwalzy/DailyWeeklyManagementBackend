import typing as tp

from fastapi.responses import JSONResponse


class MyGlobalResponse(JSONResponse):
    def render(self, content: tp.Any) -> bytes:
        r = {"code": self.status_code}
        if 200 <= self.status_code < 300:
            r['data'] = content
        else:
            r['msg'] = content

        self.status_code = 200
        return super().render(r)
