#from app.database import SESSION
from pydantic import BaseModel
from typing import Optional
#from fastapi.requests import Request
#from sqlalchemy import INT, VARCHAR, Column
from pydantic import BaseModel, Field
#from sqlalchemy.ext.declarative import declarative_base


#Base = declarative_base()
#
#
#class Fruit(BASE):
#
#    __tablename__ = "fruit"
#
#    name = Column(VARCHAR, primary_key=True)
#    count = Column(INT, nullable=False)
#
#    def dumps(self):
#        return {"name": self.name, "count": self.count}
#
#
#def init_db():
#    SESSION.merge(Fruit(**{"name": "apple", "count": 1}))
#    SESSION.commit()



#from datetime import datetime as dt
#from pytz import timezone as tz


#class queryResultSchema(Base):
#    __tablename__ = "query_results"
#
#    id = Column(INT, primary_key=True)
#    query = Column(VARCHAR)
#    num_results = Column(INT, nullable=False)
#    status = Column(INT, nullable=False)
#    query_entries = Column(VARCHAR)
#    query_timestamp = Column(VARCHAR)
#    
#    #query: str
#    #num_results: int
#    #status: int
#    #query_results: str
#    #query_timestamp: str
#    #title: str = Field(..., min_length=3, max_length=50)  # additional validation for the inputs
#    #created_date: str = dt.now(tz("Africa/Nairobi")).strftime("%Y-%m-%d %H:%M")
#
#
#class queryResultDB(queryResultSchema):
#    id: str


class arxivRequest(BaseModel):
    author: Optional[str]=None
    journal: Optional[str]=None
    title: Optional[str]=None


class queriesRequest(BaseModel):
    query_timestamp_start: str
    query_timestamp_end: str


