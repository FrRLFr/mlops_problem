from sqlalchemy import (Column, Integer, String, TIMESTAMP, Table, create_engine, MetaData, JSON)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine import Engine

from dotenv import load_dotenv
from databases import Database
#from datetime import datetime as dt
#from pytz import timezone as tz

load_dotenv()
# Database url if none is passed the default one is used
#DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://ml_user:ml_password@localhost/ml_db")
DATABASE_URL = "postgresql://ml_user:ml_password@postgres/ml_db"

# SQLAlchemy
engine: Engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SESSION: Session = sessionmaker(bind=engine)()

metadata = MetaData()
query_results = Table(
    "query_results",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("query", String),
    Column("num_results", Integer),
    Column("status", Integer, default="False"),
    Column("query_entries", JSON),
    Column("query_timestamp", TIMESTAMP))


    #id
    #query
    #num_results
    #status
    #query_timestamp
    #entries
    
    # access the third entry in the feed (random choice)
    #feed_entry_i = feed.entries[2]
    
    # access author information (returned as list)
    #list_of_authors = [author.get("name") for author in feed_entry_i.get("authors")]
    #authors = ", ".join(list_of_authors) ##authors
    
    # access title information
    #title = feed_entry_i.get("title") ###title
    
    # access journal information
    #journal = feed_entry_i.get("arxiv_journal_ref") ##journal

    #Column("created_date", String(50), default=dt.now(tz("Africa/Nairobi")).strftime("%Y-%m-%d %H:%M"))

# Databases query builder

database = Database(DATABASE_URL)