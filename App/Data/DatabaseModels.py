from sqlite3 import Date
from .Database import Base
from sqlalchemy import Column, Integer, String

class Zorgverlener(Base):
    __tablename__ = "Zorgverleners"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    email = Column(String(50), unique=False, nullable=False)
    phoneNumber = Column(Integer, nullable=False)
    password = Column(String(50), nullable=False)
    profession = Column(String(50), nullable=False)
    
class Resultaat(Base):
    __tablename__ = "Resultaten"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(50), nullable=False)
    Date = Column(String(50), nullable=False)
    Discroption = Column(String(100), unique=False, nullable=False)
    #onderzoek fk