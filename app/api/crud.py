
from loguru import logger

from datetime import datetime 
from sqlalchemy import func
from sqlalchemy import select

# my stuff
from app.db import database, query_results



async def post(payload):
    query = query_results.insert().values(
                    query=payload['query'],
                    num_results=int(payload['num_results']), 
                    status=int(payload['status']),
                    query_entries=payload['query_entries'],
                    query_timestamp=datetime.strptime(payload['query_timestamp'],"%a, %d %b %Y %H:%M:%S %Z"))
    #query_results = Table(
    #    "query_results",
    #    metadata,
    #    Column("id", Integer, primary_key=True),
#    Column("query", String(50)),
#    Column("num_results", Integer),
#    Column("status", Integer, default="False"),
#    Column("query_timestamp", TIMESTAMP))
    return await database.execute(query=query)



async def get_queries(query_timestamp_start: str, query_timestamp_end):
    query = select(query_results.c.query,
                query_results.c.query_timestamp ,
                query_results.c.status,
                query_results.c.num_results)\
        .where((query_results.c.query_timestamp >= query_timestamp_start) \
            & (query_results.c.query_timestamp <= query_timestamp_end))\
        .order_by(query_results.c.query_timestamp) ##!!! storage timestamp??
    
    return await database.fetch_all(query=query) 
    



async def get_results():
    query = select(func.json_array_elements(query_results.c.query_entries).op('->>')('authors').label('authors'),
                func.json_array_elements(query_results.c.query_entries).op('->>')('title').label('title'),
                func.json_array_elements(query_results.c.query_entries).op('->>')('journal').label('journal'))\
        .order_by(query_results.c.query_timestamp)
    
    
    return await database.fetch_all(query=query) 


