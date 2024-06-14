from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from App.Data.database import get_db
from App.Repos.appointment_repo import AppointmentRepo as appointmentrepo
from ..Models.appointment_model import Appointment


router = APIRouter()

@router.get("/appointments/")
def get_appointments(db: Session = Depends(get_db)):
    appointments = appointmentrepo.get_appointments(db)
    return appointments

@router.get("/appointments/{id}")
def get_appointmentById(id: int, db: Session = Depends(get_db)):
    appointment = appointmentrepo.get_appointment_by_id(id, db)
    return appointment

@router.post("/appointments/")
def create_appointment(appointment: Appointment, db: Session = Depends(get_db)):
    new_appointment = appointmentrepo.create_appointment(appointment, db)
    return new_appointment

@router.put("/appointments/{id}")
def update_appointment(id: int, appointment: Appointment, db: Session = Depends(get_db)):
    updated_appointment = appointmentrepo.update_appointment(id, appointment, db)
    return updated_appointment

@router.delete("/appointments/{id}")
def delete_appointment(id: int, db: Session = Depends(get_db)):
    isDeleted = appointmentrepo.delete_appointment(id, db)
    if isDeleted:
        return f"Appointment with id: {id} has been deleted."
