from sqlalchemy.orm import Session
from ..Models.PatientModel import Patient 
from App.Data import DatabaseModels as dbmodels

class PatientRepo:
    def __init__(self, db: Session):
        self.db = db

    async def patientExists(self, id: int):
        return self.db.query(dbmodels.Patient).filter(dbmodels.Patient.id == id).count()

    async def get_patients(self):
        return self.db.query(dbmodels.Patient).all()

    async def get_patient(self, id: int):
        return self.db.query(dbmodels.Patient).filter(dbmodels.Patient.id == id).first()

    async def add_patient(self, patient: Patient):
        patient.id = None
        new_patient = dbmodels.Patient(**patient.dict())
        self.db.add(new_patient)
        self.db.commit()
        self.db.refresh(new_patient)
        return new_patient

    async def update_patient(self, id: int, patient: Patient):
        patient.id = id
        patient_data = patient.dict(exclude_unset=True)
        self.db.query(dbmodels.Patient).filter(dbmodels.Patient.id == id).update(patient_data)
        self.db.commit()
        return await self.get_patient(id)

    async def delete_patient(self, id: int):
        deleted_count = self.db.query(dbmodels.Patient).filter(dbmodels.Patient.id == id).delete()
        self.db.commit()
        return deleted_count > 0