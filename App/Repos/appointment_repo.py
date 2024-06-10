from sqlalchemy import create_engine, Table, MetaData, Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from datetime import datetime

Base = declarative_base()

class Appointment(Base):
    __tablename__ = 'appointment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    description = Column(String(255))
    location = Column(String(255))
    department = Column(String(255))
    date = Column(DateTime)

    def __repr__(self):
        return "<Appointment(id= '%s', name='%s', description='%s', location='%s' department='%s' date='%s')>" % (
            self.id,
            self.name,
            self.description,
            self.location, 
            self.department,
            self.date
        )

engine = create_engine('mysql+pymysql://root:rootpassword@127.0.0.1:3306/B2C6')
Session = sessionmaker(bind=engine)
session = Session()

# CRUD functionaliteiten 
def create_appointment(appointment: Appointment):
    if not all([appointment.id, appointment.name, appointment.description, appointment.location, appointment.department, appointment.date]):
        raise HTTPException(status_code=400, detail="All fields must be filled")
    try:
        session.add(appointment)
        session.commit()
        return appointment
    except SQLAlchemyError as e:
        print(f"Error: {e}")

def read_appointment(id: int):
    appointment = session.query(Appointment).filter(Appointment.id == id).first()
    if appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

def update_appointment(id: int, appointment: Appointment):
    try:
        updated_appointment = session.query(Appointment).filter(Appointment.id == id).update({Appointment.name: appointment.name})
        session.commit()
        return updated_appointment(id)
    except SQLAlchemyError as e:
        print(f"Error: {e}")

def delete_appointment(id: int):
    try:
        session.query(Appointment).filter(Appointment.id == id).delete()
        session.commit()
    except SQLAlchemyError as e:
        print(f"Error: {e}")
