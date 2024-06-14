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

engine = create_engine('mariadb+mariadbconnector://Yurr:YurrPassword@163.123.183.82:10025/B2C6')
Session = sessionmaker(bind=engine)
session = Session()

# CRUD functionaliteiten 
def create_appointment(name: str, description: str, location: str, department: str, date: datetime):
    appointment = Appointment(
        name=name,
        description=description,
        location=location,
        department=department,
        date=date
    )
    try:
        session.add(appointment)
        session.refresh()
        session.commit()
        return appointment
    except SQLAlchemyError as e:
        print(f"Error: {e}")

def read_appointment(id: int):
    appointment = session.query(Appointment).filter(Appointment.id == id).first()
    if appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found!")
    return appointment

def update_appointment(id: int, name: str, description: str, location: str, department: str, date: datetime):
    try:
        update_appointment = session.query(Appointment).filter(Appointment.id == id).update({
            Appointment.name: name,
            Appointment.description: description,
            Appointment.location: location,
            Appointment.department: department,
            Appointment.date: date
        })
        if update_appointment == 0:
            raise HTTPException(status_code=404, detail="Appointment not found!")
        session.commit()
        return session.query(Appointment).filter(Appointment.id == id).first()
    except SQLAlchemyError as e:
        print(f"Error: {e}")

def delete_appointment(id: int):
    try:
        delete_appointment = session.query(Appointment).filter(Appointment.id == id).delete()
        if delete_appointment == 0:
            raise HTTPException(status_code=404, detail="Appointment not found!")
        if delete_appointment == 1:
            session.commit()
            raise HTTPException(status_code=404, detail="Appointment succesfully deleted!")
    except SQLAlchemyError as e:
        print(f"Error: {e}")

def readall_appointments():
    try:
        appointments = session.query(Appointment).all()
        return appointments
    except SQLAlchemyError as e:
        print(f"Error: {e}")
