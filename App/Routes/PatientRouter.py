# # App/Routers/patient_router.py
# import uuid
# from fastapi import APIRouter, HTTPException
# from typing import List
# from ..Services.PatientCRUD import create_patient, get_patient_by_id, update_patient, delete_patient
# from App.Models.Patient import Patient

# router = APIRouter()

# @router.post("/patients/")
# def create_new_patient(patient_data: Patient):
#     #patient_data.id = uuid.uuid4()
#     patient_data = create_patient(patient_data)
#     print (patient_data.id)
#     return patient_data

# @router.get("/patients/{patient_id}")
# def get_patient(patient_id: str):
#     patient = get_patient_by_id(patient_id)
#     if patient:
#         return patient
#     else:
#         raise HTTPException(status_code=404, detail="Patient not found")

# @router.put("/patients/{patient_id}")
# def update_existing_patient(patient_id: str, updated_data: Patient):
#     updated_patient = update_patient(patient_id, updated_data)
#     if updated_patient:
#         return updated_patient
#     else:
#         raise HTTPException(status_code=404, detail="Patient not found")

# @router.delete("/patients/{patient_id}")
# def delete_existing_patient(patient_id: str):
#     deleted = delete_patient(patient_id)
#     if deleted:
#         return {"message": "Patient deleted successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Patient not found")

# App/Routers/patient_router.py
# import uuid
# from fastapi import APIRouter, HTTPException
# from typing import List
# from ..Services.PatientCRUD import create_patient, get_patient_by_id, update_patient, delete_patient
# from App.Models.PatientModel import Patient

# router = APIRouter()

# @router.post("/patients/")
# def create_new_patient(patient_data: Patient):
#     patient_data.id = str(uuid.uuid4())
#     return create_patient(patient_data)

# @router.get("/patients/{patient_id}")
# def get_patient(patient_id: str):
#     patient = get_patient_by_id(patient_id)
#     if patient:
#         return patient
#     else:
#         raise HTTPException(status_code=404, detail="Patient not found")

# @router.put("/patients/{patient_id}")
# def update_existing_patient(patient_id: str, updated_data: Patient):
#     updated_patient = update_patient(patient_id, updated_data)
#     if updated_patient:
#         return updated_patient
#     else:
#         raise HTTPException(status_code=404, detail="Patient not found")

# @router.delete("/patients/{patient_id}")
# def delete_existing_patient(patient_id: str):
#     deleted = delete_patient(patient_id)
#     if deleted:
#         return {"message": "Patient deleted successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Patient not found")


from fastapi import APIRouter, Depends, HTTPException, status
from ..Models.PatientModel import Patient
from sqlalchemy.orm import Session
from App.Data.Database import get_db #import get_db
from ..Repos.PatientRepo import PatientRepo

router = APIRouter(
  prefix="/patients"
)

@router.get("")
async def get_patients(db: Session = Depends(get_db)):
  Patient = await PatientRepo(db).get_patients()
  return Patient

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
  return await repo.get_patient(id)
    
@router.delete("/{id}")
async def delete_patient(id: int, db: Session = Depends(get_db)):
  repo = PatientRepo(db)
  isDeleted = await repo.delete_patient(id)

  if isDeleted:
     return f"Patient with id:{id} has been removed succesfuly!"
  
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Patient with id:{id} not found or doesn't exist!")