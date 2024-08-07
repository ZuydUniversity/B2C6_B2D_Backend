from .Database import Base
from App.Data.Database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Zorgverlener(Base):
    __tablename__ = "zorgverleners"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    email = Column(String(50), unique=False, nullable=False)
    phoneNumber = Column(String(15), nullable=False)
    password = Column(String(50), nullable=False)
    profession = Column(String(50), nullable=False)
    isActive = Column(Boolean(True), nullable=False)

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


class Verslag(Base):
    __tablename__ = "verslagen"
#is null?
    id = Column(Integer, primary_key=True, index=True)
    date= Column(String(100), index=True)
    healthcomplaints = Column(String(500), index=True)
    medicalhistory = Column(String(500), index=True)
    diagnose = Column(String(100), index=True)
    zorgverlener_id = Column(Integer, index=True, nullable=True)
    patient_id = Column(Integer, index=True, nullable=True)
