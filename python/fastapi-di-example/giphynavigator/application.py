from fastapi import FastAPI

from .containers import Container
from . import endpoints


def creat_app() -> FastAPI:
    container = Container()
    container.config.giphy.api_key.from_env("GIPHY_API_KEY")

    app = FastAPI()
    setattr(app, "container", container)
    app.include_router(endpoints.router)
    return app


app = creat_app()
