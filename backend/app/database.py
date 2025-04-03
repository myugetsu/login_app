# apps/backend/src/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.pool import StaticPool
from typing import Generator

# SQLite configuration for development
DATABASE_URL = "sqlite:///./ventry_auth.db"

# Create engine with StaticPool for SQLite thread safety
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()

# Database session dependency
def get_db() -> Generator[Session, None, None]:
    """
    Dependency that creates a new database session for each request
    and closes it after the request is completed
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
