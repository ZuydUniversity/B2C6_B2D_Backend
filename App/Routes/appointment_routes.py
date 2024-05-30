from fastapi import APIRouter, HTTPException
from typing import List, Optional
from ..Models.appointment_model import Appointment

router = APIRouter()

sim_data: List[Appointment] = []

@router.post("/appointments/", response_model= Appointment)
def create_appointment(appointment: Appointment):
    sim_data.append(appointment)
    return appointment

@router.get("/appointments/", response_model=List[Appointment])
def read_appointments():
    return sim_data

@router.get("/appointments/{appointment_id}", response_model=Appointment)
def read_appointment(appointment_id: int):
    for appointment in sim_data:
        if appointment.id == appointment_id:
            return appointment
        
@router.put("/appointments/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: int, appointment: Appointment):
    for index, existing_appointment in enumerate(sim_data):
        if existing_appointment.id == appointment_id:
            sim_data[index] = appointment
            appointment.id = appointment_id
            return appointment
    raise HTTPException(status_code=404, detail="Appointment not found")   
