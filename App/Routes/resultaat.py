from App.Repos.ResultaatRepo import ResultaatRepo
from fastapi import APIRouter, Depends, HTTPException, status
#from uuid import UUID
from App.Models.resultaat import Resultaat
from App.Data.Database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix ="/resultaten")


#get all
@router.get("/")
async def GetAll_Resultaat(db: Session = Depends(get_db)):
    return await ResultaatRepo(db).GetAll_Resultaat()

#get with id
@router.get("/{id}")
async def Get_Resultaat(id:int, db: Session = Depends(get_db)):
    return await ResultaatRepo(db).Get_Resultaat(id)

#post one
@router.post("/")
async def add_Resultaat(resultaat: Resultaat, db: Session = Depends(get_db)):
    return await ResultaatRepo(db).add_Resultaat(resultaat)

#delete by id
# @router.delete("/resultaat/{id}", response_model=dict)
# async def delete_resultaat(id: UUID):
#     resultaat_delete_by_id(id)  
#     return {"detail": "Resultaat is met succes verwijderd"}
@router.put("/{id}")
async def update_Resultaat(id: int, resultaat: Resultaat, db: Session = Depends(get_db)):
    repo = ResultaatRepo(db)
    updated_resultaat = await repo.update_Resultaat(id, resultaat)
    if not updated_resultaat:
        raise HTTPException(status_code=404, detail="Resultaat not found")
    return updated_resultaat