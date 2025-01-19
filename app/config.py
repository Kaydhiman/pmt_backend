from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv

DB_URL = getenv("DB_URL")
JWT_SECRET = getenv("JWT_SECRET")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)