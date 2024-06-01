# App/Routers/patient_router.py
import uuid
from fastapi import APIRouter, HTTPException
from typing import List
from ..Services.PatientCRUD import create_patient, get_patient_by_id, update_patient, delete_patient
from App.Models.Patient import Patient

router = APIRouter()

@router.post("/patients/")
def create_new_patient(patient_data: Patient):
    #patient_data.id = uuid.uuid4()
    patient_data = create_patient(patient_data)
    print (patient_data.id)
    return patient_data

@router.get("/patients/{patient_id}")
def get_patient(patient_id: str):
    patient = get_patient_by_id(patient_id)
    if patient:
        return patient
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

@router.put("/patients/{patient_id}")
def update_existing_patient(patient_id: str, updated_data: Patient):
    updated_patient = update_patient(patient_id, updated_data)
    if updated_patient:
        return updated_patient
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

@router.delete("/patients/{patient_id}")
def delete_existing_patient(patient_id: str):
    deleted = delete_patient(patient_id)
    if deleted:
        return {"message": "Patient deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Patient not found")
