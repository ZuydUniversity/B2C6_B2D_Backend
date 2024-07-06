from App.Repos.ResultaatRepo import ResultaatRepo
from fastapi import APIRouter, Depends, HTTPException, status
from App.Models.resultaat import ResultaatIn, ResultaatOut
from App.Data.Database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix ="/resultaten")


@router.get("/", response_model=list[ResultaatOut])
async def GetAll_Resultaat(db: Session = Depends(get_db)):
    return await ResultaatRepo(db).GetAll_Resultaat()

@router.get("/{id}", response_model=ResultaatOut)
async def Get_Resultaat(id:int, db: Session = Depends(get_db)):
    return await ResultaatRepo(db).Get_Resultaat(id)

@router.post("/", response_model=ResultaatOut)
async def add_Resultaat(resultaat: ResultaatIn, db: Session = Depends(get_db)):
    return await ResultaatRepo(db).add_Resultaat(resultaat)

@router.put("/{id}", response_model=ResultaatOut)
async def update_Resultaat(id: int, resultaat: ResultaatIn, db: Session = Depends(get_db)):
    updated_resultaat = await ResultaatRepo(db).update_Resultaat(id, resultaat)
    if not updated_resultaat:
        raise HTTPException(status_code=404, detail="Resultaat not found")
    return updated_resultaat


@router.delete("/{id}", response_model=dict)
async def delete_Resultaat(id: int, db: Session = Depends(get_db)):
    await ResultaatRepo(db).delete_Resultaat(id)
    return {"detail": "Resultaat is met succes verwijderd"}
