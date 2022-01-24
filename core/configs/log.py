# from uvicorn.config import LOGGING_CONFIG as UVICORN_LOGGING_CONFIG

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',  # noqa: E501
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "daily": {
            "formatter": "default",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "logs/app.log",
            "when": "midnight",
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["default", "daily"], "level": "INFO"},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access", ], "level": "INFO", "propagate": False},
    },
}
