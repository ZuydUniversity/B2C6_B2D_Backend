from sqlalchemy.orm import Session
from ..Models.VerslagModel import Verslag 
from App.Data import DatabaseModels as dbmodels

class VerslagenRepo:
    def __init__(self, db: Session):
        self.db = db


    def add_verslag(db_session: Session, date, healthcomplaints, medicalhistory, diagnose): #run python -m backend.main
        verslag = Verslag(
            date=date,
            healthcomplaints=healthcomplaints,
            medicalhistory=medicalhistory,
            diagnose=diagnose
        )
        db_session.add(verslag)
        db_session.commit()
        db_session.refresh(verslag)
        return verslag

    def get_verslag(db_session: Session, verslag_id):
        return db_session.query(Verslag).filter(Verslag.id == verslag_id).first()
    
    def get_verslagen(db_session: Session):
        return db_session.query(Verslag).all()

    def update_verslag(db_session: Session, verslag_id, date=None, healthcomplaints=None, medicalhistory=None, diagnose=None):
        verslag = db_session.query(Verslag).filter(Verslag.id == verslag_id).first()
        if verslag:
            if date:
                verslag.date = date
            if healthcomplaints:
                verslag.healthcomplaints = healthcomplaints
            if medicalhistory:
                verslag.medicalhistory = medicalhistory
            if diagnose:
                verslag.diagnose = diagnose
            db_session.commit()
            db_session.refresh(verslag)
        return verslag
    
    def delete_verslag(db_session: Session, verslag_id):
        verslag = db_session.query(Verslag).filter(Verslag.id == verslag_id).first()
        if verslag:
            db_session.delete(verslag)
            db_session.commit()
        return verslag
    

    




