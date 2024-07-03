# from fastapi import APIRouter, Depends, HTTPException, status
# from ..Models.PatientModel import Patient
# from sqlalchemy.orm import Session
# from App.Data.Database import get_db
# from ..Repos.PatientRepo import PatientRepo

# router = APIRouter(
#   prefix="/patients"
# )

# @router.get("")
# async def get_patients(db: Session = Depends(get_db)):
#   Patient = await PatientRepo(db).get_patients()
#   return Patient

# @router.get("/{id}")
# async def get_patientById(id: int, db: Session = Depends(get_db)):
#   repo = PatientRepo(db)

#   exists = await repo.patientExists(id)
#   if exists < 1:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail=f"Patient with id:{id} not found or doesn't exist!")
  
#   return await repo.get_patient(id)

# @router.post("")
# async def add_patient(patient: Patient, db: Session = Depends(get_db)):
#   repo = PatientRepo(db)
#   newPatient = await repo.add_patient(patient)
#   return f"New Patient with id:{newPatient.id} created!"

# @router.put("/{id}")
# async def update_patient(id:int, patient: Patient, db: Session = Depends(get_db)):
#   repo = PatientRepo(db)
#   exists = await repo.patientExists(id)
  
#   if exists < 1:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail=f"Patient with id:{id} not found or doesn't exist!")
  
#   await repo.update_patient(id, patient)
#   return await repo.get_patient(id)
    
# @router.delete("/{id}")
# async def delete_patient(id: int, db: Session = Depends(get_db)):
#   repo = PatientRepo(db)
#   isDeleted = await repo.delete_patient(id)
 
#   if isDeleted:
#      return f"Patient with id:{id} has been removed succesfuly!"
  
#   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                         detail=f"Patient with id:{id} not found or doesn't exist!")


# patientrouter.py

from fastapi import APIRouter, Depends, HTTPException, status
from ..Models.PatientModel import Patient
from sqlalchemy.orm import Session
from App.Data.Database import get_db
from ..Repos.PatientRepo import PatientRepo

router = APIRouter(
    prefix="/patients"
)

@router.get("")
async def get_patients(db: Session = Depends(get_db)):
    repo = PatientRepo(db)
    return await repo.get_patients()

@router.get("/{id}")
async def get_patient(id: int, db: Session = Depends(get_db)):
    repo = PatientRepo(db)
    patient = await repo.get_patient(id)
    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Patient with id {id} not found")
    return patient

@router.post("")
async def add_patient(patient: Patient, db: Session = Depends(get_db)):
    repo = PatientRepo(db)
    return await repo.add_patient(patient)

@router.put("/{id}")
async def update_patient(id: int, patient: Patient, db: Session = Depends(get_db)):
    repo = PatientRepo(db)
    updated_patient = await repo.update_patient(id, patient)
    if not updated_patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Patient with id {id} not found")
    return updated_patient

@router.delete("/{id}")
async def delete_patient(id: int, db: Session = Depends(get_db)):
    repo = PatientRepo(db)
    deleted = await repo.delete_patient(id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Patient with id {id} not found")
    return {"detail": f"Patient with id {id} deleted successfully"}
