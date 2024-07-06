from App.Models.spiersterkte import SpiersterkteIn, SpiersterkteOut
from App.Data.Database import get_db
from App.Repos.SpiersterkteRepo import SpiersterkteRepo
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/spiersterkten")


@router.get("/", response_model=list[SpiersterkteOut])
async def GetAll_Spiersterkte(db: Session = Depends(get_db)):
    return await SpiersterkteRepo(db).GetAll_Spiersterkte()


@router.get("/{id}", response_model=SpiersterkteOut)
async def Get_Spiersterkte(id:int, db: Session = Depends(get_db)):
    return await SpiersterkteRepo(db).Get_Spiersterkte(id)


@router.post("/", response_model=SpiersterkteOut)
async def add_Spiersterkte(spiersterkte: SpiersterkteIn, db: Session = Depends(get_db)):
    return await SpiersterkteRepo(db).add_Spiersterkte(spiersterkte)


@router.put("/{id}", response_model=SpiersterkteOut)
async def update_Spiersterkte(
    id: int, spiersterkte: SpiersterkteIn, db: Session = Depends(get_db)
):
    updated_spiersterkte = await SpiersterkteRepo(db).update_Spiersterkte(
        id, spiersterkte
    )
    if not updated_spiersterkte:
        raise HTTPException(status_code=404, detail="Spiersterkte not found")
    return updated_spiersterkte


@router.delete("/{id}", response_model=dict)
async def delete_Spiersterkte(id: int, db: Session = Depends(get_db)):
    await SpiersterkteRepo(db).delete_Spiersterkte(id)
    return {"detail": "Spiersterkte is met succes verwijderd"}
