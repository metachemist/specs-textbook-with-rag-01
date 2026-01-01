from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, create_engine as sqlmodel_create_engine
from .config import settings

# Create the database engine using SQLModel
engine = sqlmodel_create_engine(
    settings.DATABASE_URL,
    echo=True  # Set to True for SQL query logging
)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    """
    Dependency function to get database session
    """
    session = Session(bind=engine)
    try:
        yield session
    finally:
        session.close()