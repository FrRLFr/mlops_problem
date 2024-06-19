from fastapi import APIRouter, HTTPException, Response
from loguru import logger
#from app.main import logger

# for accessing arxiv
import feedparser
import requests
import json

# my stuff
from app.api.crud import post
from app.api.models import arxivRequest 



router = APIRouter()

@router.post("/{max_query_results}")
#def search_arxiv(max_query_results: int, your_custom_query: Union[str, None] = None, request: arxivRequest):
async def search_arxiv(max_query_results: int, request:arxivRequest =None): 
    logger.info(f"Arvix endpoint accessed")
    
    if request is None:
        raise HTTPException(status_code=400, detail= "Must provide one of author, journal, title")

    request_json = request.model_dump()
    #request_json = await request.json() 
    
    query_raw = []
    
    ## check for none set
    for key in request.model_fields_set:
        query_raw.append(key + ':\\"' + request_json[key] + '\\"')
    

    query_connect ='AND'.join(query_raw)
    
    your_custom_query = query_connect.replace("title","ti").replace("author","au")
    
    # compose URL for arxiv.org API
    url = f"https://export.arxiv.org/api/query?search_query={your_custom_query}&skip=0&max_results={max_query_results}&sortBy=relevance&sortOrder=descending"
    
    try:
        response = requests.get(url, verify=False)
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=404, detail="No response from arvix")
        
        
    
    #ordering
    # handle emtpy result
    # handle arxiv not avail
    
    # add OpenSearch specification to _FeedParserMixin.namespace under key 'opensearch', which defines a standard for
    # representing search results in RSS or Atom feeds
    feedparser.mixin._FeedParserMixin.namespaces["http://a9.com/-/spec/opensearch/1.1/"] = "opensearch"
    # add arxiv namespace to _FeedParserMixin.namespace under key 'arxiv', which defines the arXiv Atom feed
    feedparser.mixin._FeedParserMixin.namespaces["http://arxiv.org/schemas/atom"] = "arxiv"

    # parse response content
    feed = feedparser.parse(response.content)
    
    # access the query
    query = feed.get("feed").get("title")
    
    # access the total number of results
    total_results = feed.get("feed").get("opensearch_totalresults")
    
    # access the response status code
    status = response.status_code ###!!! int status
    
    # access the time of the query
    query_timestamp_str = response.headers["Date"] ### !!!
    
    # access any of the results in the feed
    entries = feed.entries  ##!!! query results
    
    if int(total_results)==0:
        raise HTTPException(status_code=404, detail="Error in finding entries")
    
    dict_entries = []
    for entry in entries:
        list_of_authors = [author.get("name") for author in entry.get("authors")]
        authors = ", ".join(list_of_authors)
        title = entry.get("title")
        journal = entry.get("arxiv_journal_ref")
        dict_entries.append(
            {"authors":authors,
             "title":title,
             "journal":journal}
        )
    
    ## save query, timestamp when query made, status code, num_results that were returned
    payload = {
        "query":query,
        "num_results":total_results,
        "status":status,
        "query_timestamp":query_timestamp_str,
        "query_entries":dict_entries
    }
    
    query_result_id = await post(payload)
    
    response_object = {
        "id": query_result_id,
        'query':payload['query'],
        'num_results':int(payload['num_results']), 
        'status':payload['status'],
        'query_entries':payload['query_entries'],
        'query_timestamp':payload['query_timestamp']}
    output_edit=json.dumps(response_object, indent=4)
    return Response(content=output_edit, media_type='application/json')



#Mon, 17 Jun 2024 07:15:53 GMT
