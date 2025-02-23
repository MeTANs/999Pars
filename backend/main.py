import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

import settings 
from db import models
from db.session import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title="Web data analysing",
    lifespan=lifespan
    )





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=settings.APP_PORT, reload=True)