from contextlib import asynccontextmanager

from fastapi import FastAPI
#from starlette.middleware.cors import CORSMiddleware
from fastapi.requests import Request
#from loguru import logger
#import logging

from app.db import metadata, database, engine
from app.api import arxiv, queries, results



metadata.create_all(engine) 



# database connection
@asynccontextmanager
async def lifespan(_app:FastAPI):
    try:
        await database.connect()
        yield
    finally:
        #logger.info('Shutting down')
        await database.disconnect()



app = FastAPI(
    lifespan=lifespan)

#origins = [
#    "http://localhost",
#    "http://app:8080",
#    "http://localhost:5173",
#    "http://postgres:5432",
#    "*"
#]
#
#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=["*"],
#    allow_credentials=True,
#    allow_methods=["DELETE", "GET", "POST", "PUT"],
#    allow_headers=["*"],
#)


#include endpoints
app.include_router(arxiv.router, prefix="/arxiv", tags=["arxiv"])
app.include_router(queries.router, prefix="/queries", tags=["queries"])
app.include_router(results.router, prefix="/results", tags=["results"])


