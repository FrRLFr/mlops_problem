import pytest
import asyncio
#from pytest import pytest_asyncio
#pytest_plugins = ('pytest_asyncio',)


from fastapi.testclient import TestClient
from httpx import AsyncClient
#import pathlib
#import sys

#_parentdir = pathlib.Path(__file__).parent.parent.resolve()
#sys.path.insert(0, str(_parentdir))

from app.main import app
from app.db import database

#@pytest.mark.asyncio
@pytest.fixture(scope="session")
def test_app():
    #client = TestClient(app)
    client = AsyncClient(app=app, base_url='http://test')
    #async with AsyncClient(app) as ac:

    yield client  # testing happens here
    

#@pytest.fixture(autouse=True)
#async def test_db():
#    db = await database.connect()
#
#    yield db  # testing happens here

