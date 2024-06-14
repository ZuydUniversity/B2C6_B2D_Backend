from unittest import result
from sqlalchemy.orm import Session
from ..Models.resultaat import Resultaat 
from App.Data import DatabaseModels as dbmodels

class ResultaatRepo:
    def __init__(self, db: Session):
        self.db = db   
    #create
    async def add_Resultaat(self,resultaat: Resultaat):
        resultaat.id = None
        new_resultaat = dbmodels.Resultaat(**resultaat.model_dump())
        self.db.add(new_resultaat)
        self.db.commit()
        self.db.refresh(new_resultaat)
        return new_resultaat

    #read single
    async def Get_Resultaat(self, id: int):
        Resultaat = self.db.query(dbmodels.Resultaat).filer(dbmodels.Resultaat.id == id).first()
        return Resultaat

    #read all    
    async def GetAll_Resultaat(self):
        Resultaat = self.db.query(dbmodels.Resultaat).all()
        return Resultaat

    #update

    #delete
    async def delete_Resultaat(self, id: int):
        resultaat = self.db.query(dbmodels.Resultaat).filter(dbmodels.Resultaat.id == id).first()
        if resultaat:
            self.db.delete(resultaat)
            self.db.commit()
            return True
        return False
