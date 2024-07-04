from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = "Patients"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(50), nullable=False)
    address = Column(String(50) )
    postalZip = Column(String(50) )
    phone = Column(String(50) )
    email = Column(String(50), unique=False )