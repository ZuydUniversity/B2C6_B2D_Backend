from sqlalchemy.orm import Session
from ..Models.resultaat import ResultaatBase 
from App.Data import DatabaseModels as dbmodels

class ResultaatRepo:
    def __init__(self, db: Session):
        self.db = db
        
async def add_Resultaat(self,resultaat: ResultaatBase):
    resultaat.id = None
    new_resultaat = dbmodels.Resultaat(**resultaat.model_dump())
    self.db.add(new_resultaat)
    self.db.commit()
    self.db.refresh(new_resultaat)
    return new_resultaat