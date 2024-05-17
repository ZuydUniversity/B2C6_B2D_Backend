from sqlalchemy import String, Integer, Column
from database import Base

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True)
    gender = Column(String(40))
