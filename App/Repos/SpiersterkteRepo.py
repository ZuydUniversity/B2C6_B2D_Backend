from typing import Optional

from App.Data import DatabaseModels as dbmodels
from App.Models.spiersterkte import SpiersterkteDb, SpiersterkteIn
from sqlalchemy.orm import Session


class SpiersterkteRepo:
    def __init__(self, db: Session):
        self.db = db

    # create
    async def add_Spiersterkte(self, spiersterkte: SpiersterkteIn) -> SpiersterkteDb:
        new_spiersterkte = dbmodels.Spiersterkte(**spiersterkte.model_dump())
        self.db.add(new_spiersterkte)
        self.db.commit()
        self.db.refresh(new_spiersterkte)
        return new_spiersterkte

    # read single
    async def Get_Spiersterkte(self, id: int) -> SpiersterkteDb:
        Spiersterkte = (
            self.db.query(dbmodels.Spiersterkte)
            .filter(dbmodels.Spiersterkte.id == id)
            .first()
        )
        return Spiersterkte

    # read all
    async def GetAll_Spiersterkte(self) -> list[SpiersterkteDb]:
        Spiersterkte = self.db.query(dbmodels.Spiersterkte).all()
        return Spiersterkte

    # update
    async def update_Spiersterkte(
        self, id: int, spiersterkte_data: SpiersterkteIn
    ) -> Optional[SpiersterkteDb]:
        spiersterkte = (
            self.db.query(dbmodels.Spiersterkte)
            .filter(dbmodels.Spiersterkte.id == id)
            .first()
        )
        if spiersterkte:
            for key, value in spiersterkte_data.dict(exclude_unset=True).items():
                setattr(spiersterkte, key, value)

            self.db.commit()
            self.db.refresh(spiersterkte)
            return spiersterkte

        return None

    # delete
    async def delete_Spiersterkte(self, id: int):
        OBJ = (
            self.db.query(dbmodels.Spiersterkte)
            .filter(dbmodels.Spiersterkte.id == id)
            .first()
        )
        self.db.delete(OBJ)
        self.db.commit()

        return None
