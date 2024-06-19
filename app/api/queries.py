
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, Response
from fastapi.encoders import jsonable_encoder

from datetime import datetime as dt
import json
#from app.main import logger
from loguru import logger

from app.api.crud import get_queries
from app.api.models import queriesRequest



router = APIRouter()

@router.post("/")
async def json_from_db(request:queriesRequest): 
    logger.info(f"Queries post endpoint accessed")
    
    query_timestamp_start = dt.strptime(request.query_timestamp_start, "%Y-%m-%d %H:%M:%S" )
    query_timestamp_end = dt.strptime(request.query_timestamp_end, "%Y-%m-%d %H:%M:%S")
    
        
    
    output = await get_queries(query_timestamp_start, query_timestamp_end)
    if not output:
        raise HTTPException(status_code=404, detail="No entries found")
    
    #output_edit=jsonable_encoder(output)
    output_edit=json.dumps(jsonable_encoder(output), indent=4)
    
    return Response(content=output_edit, media_type='application/json')
    


@router.get("/")
async def queries_file(request:queriesRequest): 
    logger.info(f"Queries get endpoint accessed")
    
    query_timestamp_start = dt.strptime(request.query_timestamp_start, "%Y-%m-%d %H:%M:%S" )
    query_timestamp_end = dt.strptime(request.query_timestamp_end, "%Y-%m-%d %H:%M:%S")
    
    
    output = await get_queries(query_timestamp_start, query_timestamp_end)
    if not output:
        raise HTTPException(status_code=404, detail="No entries found")
    
    with open('get_queries.json', 'w', encoding='utf-8') as f:
        #json.dumps(output_edit, f, ensure_ascii=False, indent=4)
        json.dump(jsonable_encoder(output), f, ensure_ascii=False, indent=4, default=str)

    return FileResponse('get_queries.json')
    

#curl -X POST http://0.0.0.0:8080/queries/ -d '{"query_timestamp_start":"2024-06-17 08:52:00","query_timestamp_end":"2024-06-17 08:54:00"}'
#curl -X GET http://0.0.0.0:8080/queries/ -d '{"query_timestamp_start":"2024-06-17 08:52:00","query_timestamp_end":"2024-06-17 08:54:00"}'