import pytest
#import asyncio
#from httpx import AsyncClient
#from fastapi.testclient import TestClient
#from app.main import app
from app.db import database


#client=TestClient(app)

@pytest.mark.asyncio
#@pytest.mark.webtest
#async def test_api():
async def test_api(test_app):
    #async with AsyncClient(app=app, base_url='http://test') as ac: 
    await database.connect()
    response_arxiv = await test_app.post("/arxiv/8", json={"author":"einstein"})
    await database.disconnect()
    #response_arxiv = await ac.post("/arxiv/8", json={"author":"einstein"})
        #response_results = await ac.get("/results/")
    assert response_arxiv.status_code == 200
    assert [key in ["id", "query", "num_results", "status", "query_entries"] for key in response_arxiv.json().keys()]
    #assert response_results.status_code == 200
    #assert response.json() == {"ping": "pong!"}



