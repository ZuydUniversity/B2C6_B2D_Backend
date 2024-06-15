from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = "Patients"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    postalZip = Column(String(50), nullable=False)
    phone = Column(Integer, nullable=False)
    email = Column(String(50), unique=False, nullable=False)