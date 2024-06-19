
from fastapi import APIRouter, HTTPException
from fastapi import Response
from fastapi.encoders import jsonable_encoder

from loguru import logger
import json

from app.api.crud import get_results



router = APIRouter()

@router.get("/", status_code=201)
#async def results_from_db(query_str:str=None): 
async def results_from_db(page: int = 0, items_per_page: int = 15): 
    
    logger.info(f"Results endpoint accessed with page={page} and items_per_page={items_per_page}")
    
    #query_raw = str()
    #
    #for key in request_json:
    #    query_raw += key + ':\\"' + request_json[key] + '\\"AND'
    
    
    output = await get_results()
    if not output:
        raise HTTPException(status_code=404, detail="No entries found")
    
    step_one = jsonable_encoder(output)

    if len(step_one)>page*items_per_page:
        output_pages = step_one[
            page*items_per_page:(page+1)*items_per_page
        ]
    else:
        output_pages = step_one[len(step_one)-items_per_page:]
    # access the third entry in the feed (random choice)

    ## save query, timestamp when query made, status code, num_results that were returned
        
    
    # access the third entry in the feed (random choice)

    
    output_edit=json.dumps(output_pages, indent=4)
    
    return Response(content=output_edit, media_type='application/json')



#curl -X GET http://0.0.0.0:8080/results/ 