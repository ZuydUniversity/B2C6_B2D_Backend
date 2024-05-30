from fastapi import APIRouter
from typing import List, Optional
from ..Models.appointment_model import Appointment

router = APIRouter()

sim_data: List[Appointment] = []

@router.post("/appointments/", response_model= Appointment)
def create_appointment(appointment: Appointment):
    sim_data.append(appointment)
    return appointment

