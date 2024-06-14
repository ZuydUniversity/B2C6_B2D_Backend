from fastapi import APIRouter, HTTPException
from typing import List, Optional
from ..Models.appointment_model import Appointment
from ..Repos.appointment_repo import create_appointment, read_appointment, update_appointment, delete_appointment, readall_appointments
from datetime import datetime

router = APIRouter()

@router.post("/appointments/", response_model=Appointment)
def create_appointment_route(name: str, description: str, location: str, department: str, date: datetime):
    return create_appointment(name, description, location, department, date)

@router.get("/appointments/", response_model=List[Appointment])
def read_appointments_route():
    return readall_appointments()

@router.get("/appointments/{id}", response_model=Appointment)
def read_appointment_route(id: int):
    return read_appointment(id)

@router.put("/appointments/{id}", response_model=Appointment)
def update_appointment_route(id: int, name: str, description: str, location: str, department: str, date: datetime):
    return update_appointment(id, name, description, location, department, date)

@router.delete("/appointments/{id}", response_model=Appointment)
def delete_appointment_route(id: int):
    return delete_appointment(id)