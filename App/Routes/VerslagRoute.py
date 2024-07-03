from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from App.Data.Database import get_db
from App.Repos.VerslagRepo import VerslagRepo
from ..Models.VerslagModel import Verslag as PydanticVerslag

router = APIRouter(prefix="/verslag")


@router.get("", response_model=List[PydanticVerslag])
def get_verslagen(db: Session = Depends(get_db)):
    verslagen = VerslagRepo(db).get_verslagen()
    return verslagen

@router.get("/{id}", response_model=PydanticVerslag)
def get_verslag_by_id(id: int, db: Session = Depends(get_db)):
    repo = VerslagRepo(db)
    verslag = repo.get_verslag(id)
    if not verslag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Verslag with id {id} not found")
    # Ensure all required fields are included in the response
    return verslag

@router.post("", response_model=PydanticVerslag)
def add_verslag(verslag: PydanticVerslag, db: Session = Depends(get_db)):
    repo = VerslagRepo(db)
    new_verslag = repo.add_verslag(
        date=verslag.date,
        healthcomplaints=verslag.healthcomplaints,
        medicalhistory=verslag.medicalhistory,
        diagnose=verslag.diagnose,
        zorgverlener_id=verslag.zorgverlener_id,
        patient_id=verslag.patient_id
    )
    return new_verslag

@router.put("/{id}", response_model=PydanticVerslag)
def update_verslag(id: int, verslag: PydanticVerslag, db: Session = Depends(get_db)):
    repo = VerslagRepo(db)
    existing_verslag = repo.get_verslag(id)
    if not existing_verslag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Verslag with id {id} not found")
    updated_verslag = repo.update_verslag(
        verslag_id=id,
        date=verslag.date,
        healthcomplaints=verslag.healthcomplaints,
        medicalhistory=verslag.medicalhistory,
        diagnose=verslag.diagnose,
        zorgverlener_id=verslag.zorgverlener_id,
        patient_id=verslag.patient_id
    )
    return updated_verslag

@router.delete("/{id}", response_model=dict)
def delete_verslag(id: int, db: Session = Depends(get_db)):
    repo = VerslagRepo(db)
    deleted = repo.delete_verslag(id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Verslag with id {id} not found")
    return {"message": f"Verslag with id {id} has been deleted successfully"}
