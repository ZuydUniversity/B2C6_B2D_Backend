from fastapi import APIRouter, Depends, HTTPException, status
from ..Models.PatientModel import Patient
from sqlalchemy.orm import Session
from App.Data.Database import get_db
from ..Repos.PatientRepo import PatientRepo

router = APIRouter(
  prefix="/patients",
  tags=["Patients"]
)

@router.get("")
async def get_patients(db: Session = Depends(get_db)):
  repo = PatientRepo(db)
  patients = await repo.get_patients()
  return patients

@router.get("/{id}")
async def get_patientById(id: int, db: Session = Depends(get_db)):
  repo = PatientRepo(db)
  exists = await repo.patientExists(id)
  if exists < 1:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Patient with id:{id} not found or doesn't exist!")
  
  return await repo.get_patient(id)

@router.post("")
async def add_patient(patient: Patient, db: Session = Depends(get_db)):
  repo = PatientRepo(db)
  newPatient = await repo.add_patient(patient)
  return f"New Patient with id:{newPatient.id} created!"

@router.put("/{id}")
async def update_patient(id:int, patient: Patient, db: Session = Depends(get_db)):
  repo = PatientRepo(db)
  exists = await repo.patientExists(id)
  
  if exists < 1:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Patient with id:{id} not found or doesn't exist!")
  
  await repo.update_patient(id, patient)
  return f"Patient with id:{id} updated!"

@router.delete("/{id}")
async def delete_patient(id: int, db: Session = Depends(get_db)):
  repo = PatientRepo(db)
  exists = await repo.patientExists(id)
  
  if exists < 1:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Patient with id:{id} not found or doesn't exist!")
  
  await repo.delete_patient(id)
  return f"Patient with id:{id} deleted!"