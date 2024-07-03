import logging

from fastapi import FastAPI, Request

from src import routers
from src.core.dependencies import lifespan


app = FastAPI(lifespan=lifespan)
logger = logging.getLogger(__name__)

for name in dir(routers):
    if name.startswith("__"):
        continue
    _router = getattr(routers, name)
    app.include_router(_router)
    logger.info(f"New router '{_router.prefix}' created.")


@app.get("/")
async def status_check(request: Request):
    return ""
