from sqlalchemy.orm import Session
from ..Models.PatientModel import Patient
from App.Data import DatabaseModels

class PatientRepo:
  def __init__(self, db: Session):
    self.db = db

  async def get_patients(self):
    return self.db.query(Patient).all()

  async def get_patient(self, id: int):
    return self.db.query(Patient).filter(Patient.id == id).first()

  async def patientExists(self, id: int):
    return self.db.query(Patient).filter(Patient.id == id).count()

  async def add_patient(self, patient: Patient):
    db_patient = DatabaseModels.Patient(**patient.model_dump())
    if db_patient.id == 0:
            db_patient.id = None
    self.db.add(db_patient)
    self.db.commit()
    self.db.refresh(db_patient)
    return patient

  async def update_patient(self, id: int, patient: Patient):
    db_patient = self.db.query(Patient).filter(Patient.id == id).first()
    db_patient.name = patient.name
    db_patient.address = patient.address
    db_patient.postalZip = patient.postalZip
    db_patient.phone = patient.phone
    db_patient.email = patient.email
    self.db.commit()
    self.db.refresh(db_patient)
    return db_patient

  async def delete_patient(self, id: int):
    db_patient = self.db.query(Patient).filter(Patient.id == id).first()
    self.db.delete(db_patient)
    self.db.commit()