from fastapi import APIRouter, Depends, HTTPException, status
from ..Models.ZorgverlenerModel import Zorgverlener
from sqlalchemy.orm import Session
from App.Data.Database import get_db
from ..Repos.ZorgverlenerRepo import ZorgverlenersRepo

router = APIRouter(
  prefix="/zorgverleners"
)


@router.get("")
async def get_zorgverleners(db: Session = Depends(get_db)):
  ZorgVerleners = await ZorgverlenersRepo(db).get_zorgverleners()
  return ZorgVerleners

@router.get("/{id}")
async def get_zorgverlenerById(id: int, db: Session = Depends(get_db)):
  repo = ZorgverlenersRepo(db)

  exists = await repo.zorgverlenerExists(id)
  if exists < 1:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Zorgverlener with id:{id} not fond or doesn't exist!")
  
  return await repo.get_zorgverlener(id)

@router.post("")
async def add_zorgverlener(zorgverlener: Zorgverlener, db: Session = Depends(get_db)):
  repo = ZorgverlenersRepo(db)
  newZorgverlener = await repo.add_zorgverlener(zorgverlener)
  return f"New Zorgverlener with id:{newZorgverlener.id} created!"

@router.put("/{id}")
async def update_zorgverlener(id:int, zorgverlener: Zorgverlener, db: Session = Depends(get_db)):
  repo = ZorgverlenersRepo(db)
  exists = await repo.zorgverlenerExists(id)
  
  if exists < 1:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Zorgverlener with id:{id} not fond or doesn't exist!")
  
  await repo.update_zorgverlener(id, zorgverlener)
  return await repo.get_zorgverlener(id)
    
@router.delete("/{id}")
async def delete_zorgverlener(id: int, db: Session = Depends(get_db)):
  repo = ZorgverlenersRepo(db)
  isDeleted = await repo.delete_zorgverlener(id)

  if isDeleted:
     return f"Zorgverlener with id:{id} has been removed succesfuly!"
  
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Zorgverlener with id:{id} not fond or doesn't exist!")