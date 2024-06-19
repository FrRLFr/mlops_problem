from sqlalchemy import (Column, Integer, String, TIMESTAMP, Table, create_engine, MetaData, JSON)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine import Engine

from dotenv import load_dotenv
from databases import Database

load_dotenv()
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


database = Database(DATABASE_URL)