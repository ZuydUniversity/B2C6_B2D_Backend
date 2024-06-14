from .database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Appointment(Base):
    __tablename__ = 'APPOINTMENT'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    department = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)
