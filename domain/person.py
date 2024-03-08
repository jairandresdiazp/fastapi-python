from interface.data import DataInterface
from sqlalchemy.orm import Session

class Person(DataInterface):
  
  def __init__(self, db: SessionLocal):
    self.db = db
  
  def save(self, data: dict) :
    db.add(data)
    db.commit()
    db.refresh(db_autor)
    return data
    