from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

from settings import get_database_settings

settings = get_database_settings()

def generate_uri():
    return f'mysql+pymysql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_DB}'

SQLALCHEMY_DATABASE_URI = generate_uri() or ""

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

