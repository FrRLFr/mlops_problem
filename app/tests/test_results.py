import pytest
#import asyncio
#from httpx import AsyncClient
#from fastapi.testclient import TestClient
from app.main import app
from app.db import database



@pytest.mark.asyncio
#@pytest.mark.webtest
#async def test_results():
async def test_results(test_app):
    #async with AsyncClient(app=app, base_url='http://test') as ac: 
    await database.connect()
    response_results = await test_app.get("/results/")
    await database.disconnect()
    #assert response_arxiv.status_code == 200
    #assert [key in ["id", "query", "num_results", "status", "query_entries"] for key in response_arxiv.json().keys()]
    assert response_results.status_code == 200
    #assert response.json() == {"ping": "pong!"}


