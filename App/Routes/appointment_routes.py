from fastapi import APIRouter, HTTPException
from typing import List, Optional
from ..Models.appointment_model import Appointment

router = APIRouter()

sim_data: List[Appointment] = [{
  "id": 0,
  "name": "string",
  "description": "string",
  "location": "string",
  "department": "string",
  "date": "2024-06-01T18:14:02.411Z"
}
,
{
  "id": 1,
  "name": "string",
  "description": "string",
  "location": "string",
  "department": "string",
  "date": "2025-06-01T18:14:02.411Z"
}]

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

@router.delete("/appointments/{appointment_id}", response_model=Appointment)
def delete_appointment(appointment_id: int):
    for index, appointment in enumerate(sim_data):
        if appointment.id == appointment_id:
            return sim_data.pop(index)
    raise HTTPException(status_code=404, detail="Appointment not found")    
