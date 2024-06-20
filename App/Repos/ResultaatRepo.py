from typing import Optional
from sqlalchemy.orm import Session
from ..Models.resultaat import ResultaatIn, ResultaatDb
from App.Data import DatabaseModels as dbmodels

class ResultaatRepo:
    def __init__(self, db: Session):
        self.db = db   
    #create
    async def add_Resultaat(self,resultaat: ResultaatIn) -> ResultaatDb:
        resultaat.id = None
        new_resultaat = dbmodels.Resultaat(**resultaat.model_dump())
        self.db.add(new_resultaat)
        self.db.commit()
        self.db.refresh(new_resultaat)
        return new_resultaat

    #read single
    async def Get_Resultaat(self, id: int) -> ResultaatDb:
        Resultaat = self.db.query(dbmodels.Resultaat).filter(dbmodels.Resultaat.id == id).first()
        return Resultaat

    #read all    
    async def GetAll_Resultaat(self) -> list[ResultaatDb]:
        Resultaat = self.db.query(dbmodels.Resultaat).all()
        return Resultaat

    #update
    async def update_Resultaat(self, id: int, resultaat_data: ResultaatIn) -> Optional[ResultaatDb]:
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

