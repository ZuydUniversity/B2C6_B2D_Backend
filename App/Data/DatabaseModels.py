from App.Data.Database import Base
from sqlalchemy import Column, Integer, String
from uuid import UUID
from cryptography.fernet import Fernet

key = b'zG3lH7Wzy8RoZZdfG5bJv4QZfA9f9d-6NwvL-tWQV_c='
cipher_suite = Fernet(key)

class Patient(Base):
    __tablename__ = "Patient"

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

    def encrypt(self):
        self.name = cipher_suite.encrypt(self.name.encode()).decode()
        self.surname = cipher_suite.encrypt(self.surname.encode()).decode()
        self.age = cipher_suite.encrypt(self.age.encode()).decode()
        self.gender = cipher_suite.encrypt(self.gender.encode()).decode()
        self.address = cipher_suite.encrypt(self.address.encode()).decode()
        self.city = cipher_suite.encrypt(self.city.encode()).decode()
        self.email = cipher_suite.encrypt(self.email.encode()).decode()
        self.diagnosis = cipher_suite.encrypt(self.diagnosis.encode()).decode()
        self.medication = cipher_suite.encrypt(self.medication.encode()).decode()
        self.phonenumber = cipher_suite.encrypt(self.phonenumber.encode()).decode()

    def decrypt(self):
        self.name = cipher_suite.decrypt(self.name.encode()).decode()
        self.surname = cipher_suite.decrypt(self.surname.encode()).decode()
        self.age = cipher_suite.decrypt(self.age.encode()).decode()
        self.gender = cipher_suite.decrypt(self.gender.encode()).decode()
        self.address = cipher_suite.decrypt(self.address.encode()).decode()
        self.city = cipher_suite.decrypt(self.city.encode()).decode()
        self.email = cipher_suite.decrypt(self.email.encode()).decode()
        self.diagnosis = cipher_suite.decrypt(self.diagnosis.encode()).decode()
        self.medication = cipher_suite.decrypt(self.medication.encode()).decode()
        self.phonenumber = cipher_suite.decrypt(self.phonenumber.encode()).decode()

