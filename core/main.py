import typing as tp

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware

from .configs import app as APP
from .exception_handlers import register_exception_handlers
from .extensions.schedule_jobs import change_daily_condition_at_time
from .resources import register_resources
from .responses._all import MyGlobalResponse
from .services import redis_job_store, redis_executors


def my_openapi(app):
    def f():
        if app.openapi_schema:
            return app.openapi_schema
        # Info
        contact = {
            "name": 'charon',
            "email": 'mzrwalzy@163.com',
        }
        openapi_schema = get_openapi(
            title=APP.PROJECT_NAME,
            version='0.0.1',
            # openapi_version="2.5.0",
            description='1112222333',
            routes=app.routes,
            tags=None,
            servers=None,
            terms_of_service="不知道的ToS",
            contact=contact,
        )
        openapi_schema["info"]["x-logo"] = {
            "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
        }
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    return f


def create_app(app_env='production') -> FastAPI:
    app = FastAPI(
        title=APP.PROJECT_NAME,
        description='',
        version='0.1.0',
        # openapi_url='/static/server1.json',
        default_response_class=MyGlobalResponse,
        docs_url="/",
        # redoc_url="/",
        # root_path='/api',
    )

    # app.openapi = my_openapi(app)

    # Set all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=APP.ALLOW_ORIGINS,
        allow_credentials=APP.ALLOW_CREDENTIALS,
        allow_methods=APP.ALLOW_METHODS,
        allow_headers=APP.ALLOW_HEADERS,
    )

    # register all resources
    register_resources(app)
    # register_repository()
    register_api_doc(app)
    register_exception_handlers(app)
    register_schedule_job(app)
    return app


def register_api_doc(app: FastAPI):
    @app.get("/", include_in_schema=False)
    async def redirect_typer():
        return RedirectResponse("/index.html")

    from fastapi.staticfiles import StaticFiles
    app.mount('/', StaticFiles(directory=str(APP.PROJECT_PATH / 'api_doc')), name='api_doc')


def register_schedule_job(app: FastAPI):
    scheduler = BackgroundScheduler(timezone="Asia/Shanghai", jobstores=redis_job_store, executors=redis_executors)
    scheduler.start()
    scheduler.add_job(change_daily_condition_at_time, 'interval', jobstore='redis', start_date='2022-01-24 00:00:00',
                      hours=24)
