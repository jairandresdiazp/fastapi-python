from sqlalchemy import Column, Integer, String, Sequence, Double
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
  __tablename__ = 'person'
  id = Column(Integer, Sequence('person_id_seq'), primary_key=True)
  nombre = Column(String(50))
  edad = Column(Integer)
  sexo = Column(String(1))
  peso = Column(Double)
  altura = Column(Double)