from App.Repos.SpiersterkteRepo import SpiersterkteRepo
from fastapi import APIRouter, Depends, HTTPException, status
#from uuid import UUID
from App.Models.spiersterkte import SpiersterkteIn, SpiersterkteDb
from App.Data.Database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix ="/resultaten")


#get all
@router.get("/", response_model=list[SpiersterkteDb])
async def GetAll_Spiersterkte(db: Session = Depends(get_db)):
    return await SpiersterkteRepo(db).GetAll_Spiersterkte()

#get with id
@router.get("/{id}", response_model=SpiersterkteDb)
async def Get_Spiersterkte(id:int, db: Session = Depends(get_db)):
    return await SpiersterkteRepo(db).Get_Spiersterkte(id)

#post one
@router.post("/", response_model=SpiersterkteDb)
async def add_Spiersterkte(spiersterkte: SpiersterkteIn, db: Session = Depends(get_db)):
    return await SpiersterkteRepo(db).add_Spiersterkte(spiersterkte)

@router.put("/{id}", response_model=SpiersterkteDb)
async def update_Spiersterkte(id: int, spiersterkte: SpiersterkteIn, db: Session = Depends(get_db)):
    updated_spiersterkte = await SpiersterkteRepo(db).update_Spiersterkte(id, spiersterkte)
    if not updated_spiersterkte:
        raise HTTPException(status_code=404, detail="Spiersterkte not found")
    return updated_spiersterkte


@router.delete("/{id}", response_model=dict)
async def delete_Spiersterkte(id: int, db: Session = Depends(get_db)):
    await SpiersterkteRepo(db).delete_Spiersterkte(id)
    return {"detail": "Spiersterkte is met succes verwijderd"}