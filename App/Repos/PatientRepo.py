from sqlalchemy.orm import Session
from ..Models.PatientModel import Patient 
from App.Data import DatabaseModels as dbmodels

class PatientRepo:
    def __init__(self, db: Session):
        self.db = db

    async def patientExists(self, id:int):
        return self.db.query(dbmodels.Patient).filter(dbmodels.Patient.id == id).count()

    async def get_patients(self):
        Patients = self.db.query(dbmodels.Patients).all()
        return Patients

    async def get_patients(self, id: int):
        Patient = self.db.query(dbmodels.Patient).filter(dbmodels.Patient.id == id).first()
        return Patient

    async def add_patient(self, patient: Patient):
        patient.id = None
        new_patient = dbmodels.Patient(**patient.model_dump())
        self.db.add(new_patient)
        self.db.commit()
        self.db.refresh(new_patient)
        return new_patient
    
    async def update_patient(self, id: int, patient: Patient):
        patient.id = id
        isUpdated = self.db.query(dbmodels.Patient).filter(dbmodels.Patient.id == id).update(patient.model_dump(), synchronize_session=False)
        self.db.commit()
        return isUpdated


    async def delete_patient(self, id: int):
        verwijderd = self.db.query(dbmodels.Patient).filter(dbmodels.Patient.id == id).delete()
        self.db.commit()
        return verwijderd