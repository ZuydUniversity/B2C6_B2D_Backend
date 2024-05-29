from sqlalchemy import String, Integer, Column
from database import Base

class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True)
    gender = Column(String(40))

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    date= Column(String(100), index=True)
    healthcomplaints = Column(String(500), index=True)
    medicalhistory = Column(String(500), index=True)
    diagnose = Column(String(100), index=True)
    #uiteindelijk nog notities toevoegen



