from App.Data.Database import Base
from sqlalchemy import Column, Integer, String
from uuid import UUID


class Patient(Base):
    __tablename__ = "Patient"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(50), unique=False, nullable=False)
    age = Column(Integer, nullable=True)
    address = Column(String(50), nullable=True)
    housenumber = Column(String(10), nullable=True)
    city = Column(String(50), nullable=True)
    telephonenumber = Column(Integer, nullable=True)