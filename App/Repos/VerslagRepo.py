from sqlalchemy.orm import Session
from ..Models.VerslagModel import Verslag
from App.Data import DatabaseModels as dbmodels

class VerslagRepo:
    def __init__(self, db: Session):
        self.db = db

    def verslagExists(self, id: int):
        return self.db.query(dbmodels.Verslag).filter(dbmodels.Verslag.id == id).count()

    def add_verslag(self, date, healthcomplaints, medicalhistory, diagnose):
        verslag = dbmodels.Verslag(
            date=date,
            healthcomplaints=healthcomplaints,
            medicalhistory=medicalhistory,
            diagnose=diagnose
        )
        self.db.add(verslag)
        self.db.commit()
        self.db.refresh(verslag)
        return verslag

    def get_verslag(self, verslag_id):
        return self.db.query(dbmodels.Verslag).filter(dbmodels.Verslag.id == verslag_id).first()

    def get_verslagen(self):
        return self.db.query(dbmodels.Verslag).all()

    def update_verslag(self, verslag_id, date=None, healthcomplaints=None, medicalhistory=None, diagnose=None):
        verslag = self.db.query(dbmodels.Verslag).filter(dbmodels.Verslag.id == verslag_id).first()
        if verslag:
            if date:
                verslag.date = date
            if healthcomplaints:
                verslag.healthcomplaints = healthcomplaints
            if medicalhistory:
                verslag.medicalhistory = medicalhistory
            if diagnose:
                verslag.diagnose = diagnose
            self.db.commit()
            self.db.refresh(verslag)
        return verslag

    def delete_verslag(self, verslag_id):
        verslag = self.db.query(dbmodels.Verslag).filter(dbmodels.Verslag.id == verslag_id).first()
        if verslag:
            self.db.delete(verslag)
            self.db.commit()
        return verslag
