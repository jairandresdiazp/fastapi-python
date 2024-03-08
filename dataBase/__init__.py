from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config
from model.dataBase.person import Person

DATABASE_URL = Config.dataBase
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Person.metadata.create_all(bind=engine)


def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()