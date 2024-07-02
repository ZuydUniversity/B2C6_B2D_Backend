from typing import Optional
from sqlalchemy.orm import Session
from ..Models.resultaat import ResultaatIn, ResultaatDb, ResultaatOut
from App.Data import DatabaseModels as dbmodels
import logging

LOGGER = logging.getLogger("uvicorn")

class ResultaatRepo:
    def __init__(self, db: Session):
        self.db = db
        
    async def db_to_out(self, resultaat: ResultaatDb) -> ResultaatOut:
        SPIERSTERKTEN = self.db.query(dbmodels.Spiersterkte).filter(dbmodels.Spiersterkte.resultaat_id == resultaat.id)
        RETV = ResultaatOut(name=resultaat.name, date=resultaat.date, discription=resultaat.discription, spiersterkten=SPIERSTERKTEN)

        return RETV
        
    #create
    async def add_Resultaat(self,resultaat: ResultaatIn) -> ResultaatOut:
        new_resultaat = dbmodels.Resultaat(**resultaat.model_dump())
        self.db.add(new_resultaat)
        self.db.commit()
        self.db.refresh(new_resultaat)
        
        return self.db_to_out(new_resultaat)

    #read single
    async def Get_Resultaat(self, id: int) -> ResultaatOut:
        Resultaat = self.db.query(dbmodels.Resultaat).filter(dbmodels.Resultaat.id == id).first()
        
        return self.db_to_out(Resultaat)

    #read all    
    async def GetAll_Resultaat(self) -> list[ResultaatOut]:
        Resultaten = self.db.query(dbmodels.Resultaat).all()
        
        LOGGER.info(list(map(self.db_to_out, Resultaten)))
        
        return list(map(self.db_to_out, Resultaten))

    #update
    async def update_Resultaat(self, id: int, resultaat_data: ResultaatIn) -> Optional[ResultaatOut]:
        resultaat = self.db.query(dbmodels.Resultaat).filter(dbmodels.Resultaat.id == id).first()
        if resultaat:
            for key, value in resultaat_data.dict(exclude_unset=True).items():
                setattr(resultaat, key, value)

            self.db.commit()
            self.db.refresh(resultaat)
            return self.db_to_out(resultaat)

        return None 

    #delete
    async def delete_Resultaat(self, id: int):
        OBJ = self.db.query(dbmodels.Resultaat).filter(dbmodels.Resultaat.id == id).first()
        self.db.delete(OBJ)
        self.db.commit()
        
        return None 

