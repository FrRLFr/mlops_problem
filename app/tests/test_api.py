import pytest
#import asyncio
from app.db import database


#client=TestClient(app)

@pytest.mark.asyncio
async def test_api(test_app):
    #async with AsyncClient(app=app, base_url='http://test') as ac: 
    await database.connect()
    response_arxiv = await test_app.post("/arxiv/8", json={"author":"einstein"})
    await database.disconnect()
    assert response_arxiv.status_code == 200
    assert [key in ["id", "query", "num_results", "status", "query_entries"] for key in response_arxiv.json().keys()]
    

