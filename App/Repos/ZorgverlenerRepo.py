from sqlalchemy.orm import Session
from ..Models.Zorgverlener import Zorgverlener 
from App.Data import DataBaseModels as dbmodels

class ZorgverlenersRepo:
    def __init__(self, db: Session):
        self.db = db

    async def zorgverlenerExists(self, id:int):
        return self.db.query(dbmodels.Zorgverlener).filter(dbmodels.Zorgverlener.id == id).count()

    async def get_zorgverleners(self):
        ZorgVerleners = self.db.query(dbmodels.Zorgverlener).all()
        return ZorgVerleners

    async def get_zorgverlener(self, id: int):
        ZorgVerlener = self.db.query(dbmodels.Zorgverlener).filter(dbmodels.Zorgverlener.id == id).first()
        return ZorgVerlener

    async def add_zorgverlener(self, zorgverlener: Zorgverlener):
        zorgverlener.id = None
        new_zorgverlener = dbmodels.Zorgverlener(**zorgverlener.model_dump())
        self.db.add(new_zorgverlener)
        self.db.commit()
        self.db.refresh(new_zorgverlener)
        return new_zorgverlener
    
    async def update_zorgverlener(self, id: int, zorgverlener: Zorgverlener):
        zorgverlener.id = id
        isUpdated = self.db.query(dbmodels.Zorgverlener).filter(dbmodels.Zorgverlener.id == id).update(zorgverlener.model_dump(), synchronize_session=False)
        self.db.commit()
        return isUpdated


    async def delete_zorgverlener(self, id: int):
        verwijderd = self.db.query(dbmodels.Zorgverlener).filter(dbmodels.Zorgverlener.id == id).delete()
        self.db.commit()
        return verwijderd