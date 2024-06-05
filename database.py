import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URI", "postgresql://postgres:1234@localhost:7000/rls"))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    def _get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    return next(_get_db())
