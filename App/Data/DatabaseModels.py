from .Database import Base
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