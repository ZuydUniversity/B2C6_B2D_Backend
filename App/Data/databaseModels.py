from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from cryptography.fernet import Fernet

key = b'LX5sZIVoLTEa_Cmsl8DDAFBodF5m3B6VjVSP-Gin4xc='
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

    def decrypt(self):
        self.name = cipher_suite.decrypt(self.name.encode()).decode()
        self.description = cipher_suite.decrypt(self.description.encode()).decode()
        self.location = cipher_suite.decrypt(self.location.encode()).decode()
        self.department = cipher_suite.decrypt(self.department.encode()).decode()
        