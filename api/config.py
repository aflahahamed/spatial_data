from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL with password/username and dbname
DATABASE_URL = 'postgresql://testing:testing@localhost:5432/testing'
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()

