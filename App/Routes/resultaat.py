from App.Repos.ResultaatRepo import ResultaatRepo
from fastapi import APIRouter, Depends
#from uuid import UUID
from App.Models.resultaat import Resultaat
from App.Data.Database import get_db
from sqlalchemy.orm import Session

from App.Services.dal import resultaat_get_by_id
from App.Services.dal import resultaat_delete_by_id


router = APIRouter(prefix ="/resultaten")
#get with id
@router.get("/{id}")
async def Get_Resultaat(id:int, db: Session = Depends(get_db)):
    repo = ResultaatRepo
    # check if exist
    return await repo.Get_Resultaat(id)

#get all
async def GetAll_Resultaat(db: Session = Depends(get_db)):
    Resultaten = await ResultaatRepo(db).GetAll_Resultaat()
    return Resultaten
# @router.get("/resultaat/{id}", response_model=ResultaatBase)
# async def get_resultaat(user_id: UUID):
#     return resultaat_get_by_id(user_id)

#post one
@router.post("")
async def add_Resultaat(resultaat: Resultaat, db:Session = Depends(get_db)):
    repo = ResultaatRepo(db)
    newResultaat = await repo.add_resultaat(resultaat)
    return {"resultaat_name": resultaat.name,"Resultaat_date": resultaat.date,"resultaat_discription": resultaat.discription}

#delete by id
# @router.delete("/resultaat/{id}", response_model=dict)
# async def delete_resultaat(id: UUID):
#     resultaat_delete_by_id(id)  
#     return {"detail": "Resultaat is met succes verwijderd"}