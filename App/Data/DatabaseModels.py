from .Database import Base
from sqlalchemy import Column, Integer, String
from App.Data.Database import Base
from sqlalchemy import Column, Integer, String
from uuid import UUID


class Zorgverlener(Base):
    __tablename__ = "Zorgverleners"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    email = Column(String(50), unique=False, nullable=False)
    phoneNumber = Column(Integer, nullable=False)
    password = Column(String(50), nullable=False)
    profession = Column(String(50), nullable=False)

class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(50), nullable=True)
    address = Column(String(50), nullable=True)
    city = Column(String(50), nullable=True)
    email = Column(String(50), unique=False, nullable=False)
    diagnosis = Column(String(100), nullable=True)
    medication = Column(String(100), nullable=True)
    phonenumber = Column(Integer, nullable=True)