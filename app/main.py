from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.requests import Request
#from loguru import logger
#import logging

# my stuff
from app.db import metadata, database, engine
from app.api import arxiv, queries, results


# Logs incoming request information
#async def log_request(request: Request):
#    logger.info(
#        f"[{request.client.host}:{request.client.host}] {request.method} {request.url}"
#    )
#    logger.info(f"header: {request.headers}, body: ")
#    logger.info(await request.body())

#logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
#logger = logging.getLogger(__name__)

metadata.create_all(engine) 



#  event
@asynccontextmanager
async def lifespan(_app:FastAPI):
    #_postgres_dsn = global_settings.postgres_url.unicode_string()
    try:
        # Initialize the postgres connection pool
        #_app.postgres_pool = await asyncpg.create_pool(
        #    dsn=_postgres_dsn,
        #    min_size=5,
        #    max_size=20,
        #)
        #logger.info(f"Postgres pool created: {_app.postgres_pool.get_idle_size()=}")
        #logger.info('Starting up')
        await database.connect()
        yield
    finally:
        #logger.info('Shutting down')
        await database.disconnect()



app = FastAPI(
    lifespan=lifespan)

origins = [
    "http://localhost",
    "http://app:8080",
    "http://localhost:5173",
    "http://postgres:5432",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)


app.include_router(arxiv.router, prefix="/arxiv", tags=["arxiv"])
app.include_router(queries.router, prefix="/queries", tags=["queries"])
app.include_router(results.router, prefix="/results", tags=["results"])




#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}



