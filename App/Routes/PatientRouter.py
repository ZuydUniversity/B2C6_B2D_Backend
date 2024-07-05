from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from App.Data.Database import get_db
from ..Repos.PatientRepo import PatientRepo
from ..Models.PatientModel import Patient

router = APIRouter(
    prefix="/patients"
)

@router.get("", response_model=list[Patient])
async def get_patients(db: Session = Depends(get_db)):
    patients = await PatientRepo(db).get_patients()
    return patients

@router.get("/{id}", response_model=Patient)
async def get_patient_by_id(id: int, db: Session = Depends(get_db)):
    repo = PatientRepo(db)
    exists = await repo.patientExists(id)
    if exists < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id:{id} not found or doesn't exist!")
    return await repo.get_patient(id)

@router.post("", response_model=str)
async def add_patient(patient: Patient, db: Session = Depends(get_db)):
    repo = PatientRepo(db)
    new_patient = await repo.add_patient(patient)
    return f"New Patient with id:{new_patient.id} created!"

@router.put("/{id}", response_model=Patient)
async def update_patient(id: int, patient: Patient, db: Session = Depends(get_db)):
    repo = PatientRepo(db)
    exists = await repo.patientExists(id)
    if exists < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Patient with id:{id} not found or doesn't exist!")
    await repo.update_patient(id, patient)
    return await repo.get_patient(id)

@router.delete("/{id}", response_model=str)
async def delete_patient(id: int, db: Session = Depends(get_db)):
    repo = PatientRepo(db)
    is_deleted = await repo.delete_patient(id)
    if is_deleted:
        return f"Patient with id:{id} has been removed successfully!"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Patient with id:{id} not found or doesn't exist!")