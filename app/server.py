import os
import sys
import logging
import logging.config
from api import router
from fastapi import FastAPI
from app.library.logger import RouterLoggingMiddleware

ROOT_PATH = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
logs_target = os.path.join(ROOT_PATH + "\logs", "sample.log")

# TODO: check if there is log file config, if not create a default in root folder

# Logging configuration
logging_config = {
    "version": 1,
    "formatters": {
        "json": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(process)s %(levelname)s %(name)s %(module)s %(funcName)s %(lineno)s",
        },
        "standard": {
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(process)s %(levelname)s %(name)s %(module)s %(funcName)s %(lineno)s",
            #"datefmt": "%d %b %y %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": sys.stderr,
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": logs_target,
            "formatter": "standard",
            "mode": "a",
            "encoding": "utf-8",
            "backupCount": 4,
        },
    },
    "loggers": {
        "": {  # root logger
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": False,
        },
        "my.packg": {"handlers": ["file"], "level": "INFO", "propagate": False},
    },
    "root": {"level": "DEBUG", "handlers": ["console"], "propagate": True},
}

logging.config.dictConfig(logging_config)


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Koodies FastAPI Boilerplate",
        description="Koodies FastAPI Boilerplate",
        version="1.0.0",
    )
    app_.add_middleware(RouterLoggingMiddleware, logger=logging.getLogger(__name__))
    init_routers(app_)
    return app_


app = create_app()
