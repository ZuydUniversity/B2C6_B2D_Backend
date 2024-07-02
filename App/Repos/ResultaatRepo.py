from typing import Optional
from sqlalchemy.orm import Session
from ..Models.resultaat import ResultaatIn, ResultaatDb, ResultaatOut
from App.Data import DatabaseModels as dbmodels

class ResultaatRepo:
    def __init__(self, db: Session):
        self.db = db   
    #create
    async def add_Resultaat(self,resultaat: ResultaatIn) -> ResultaatOut:
        new_resultaat = dbmodels.Resultaat(**resultaat.model_dump())
        self.db.add(new_resultaat)
        self.db.commit()
        self.db.refresh(new_resultaat)
        
        RETV = ResultaatOut(name=new_resultaat.name, date=new_resultaat.date, discription=new_resultaat.discription, spiersterkten=())
        
        return RETV

    #read single
    async def Get_Resultaat(self, id: int) -> ResultaatOut:
        Resultaat = self.db.query(dbmodels.Resultaat).filter(dbmodels.Resultaat.id == id).first()
        
        SPIERSTERKTEN = self.db.query(dbmodels.Spiersterkte).filter(dbmodels.Spiersterkte.resultaat_id == Resultaat.id)
        
        print(SPIERSTERKTEN)
        
        RETV = ResultaatOut(name=Resultaat.name, date=Resultaat.date, discription=Resultaat.discription, spiersterkten=SPIERSTERKTEN)

        return RETV

    #read all    
    async def GetAll_Resultaat(self) -> list[ResultaatOut]:
        Resultaat = self.db.query(dbmodels.Resultaat).all()
        
        
        return Resultaat

    #update
    async def update_Resultaat(self, id: int, resultaat_data: ResultaatIn) -> Optional[ResultaatOut]:
        resultaat = self.db.query(dbmodels.Resultaat).filter(dbmodels.Resultaat.id == id).first()
        if resultaat:
            for key, value in resultaat_data.dict(exclude_unset=True).items():
                setattr(resultaat, key, value)

            self.db.commit()
            self.db.refresh(resultaat)
            return resultaat

        return None 

    #delete
    async def delete_Resultaat(self, id: int):
        OBJ = self.db.query(dbmodels.Resultaat).filter(dbmodels.Resultaat.id == id).first()
        self.db.delete(OBJ)
        self.db.commit()
        
        return None 

