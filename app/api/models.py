#from app.database import SESSION
from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel



class arxivRequest(BaseModel):
    author: Optional[str]=None
    journal: Optional[str]=None
    title: Optional[str]=None


class queriesRequest(BaseModel):
    query_timestamp_start: str
    query_timestamp_end: str


