from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from cryptography.fernet import Fernet

key = b'8Si3VdwLHS3I79BT_TnxDqAKw_5vnimPHxwZycDDLrk='
cipher_suite = Fernet(key)

class Appointment(Base):
    __tablename__ = 'APPOINTMENT'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    department = Column(String(255), nullable=False)
    date = Column(DateTime, nullable=False)

    def encrypt(self):
        self.name = cipher_suite.encrypt(self.name.encode()).decode()
        self.description = cipher_suite.encrypt(self.description.encode()).decode()
        self.location = cipher_suite.encrypt(self.location.encode()).decode()
        self.department = cipher_suite.encrypt(self.department.encode()).decode()
        
