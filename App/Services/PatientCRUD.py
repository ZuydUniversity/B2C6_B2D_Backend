from typing import List
from uuid import UUID 
from App.Models.Patient import Patient

# Dummy database
database = [{
  "id": UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"),
  "name": "has2323san",
  "surname": "test555",
  "email": "string",
  "age": 0,
  "address": "string",
  "housenumber": "string",
  "city": "string",
  "telephonenumber": 0
}]

# Create-operatie
def create_patient(patient_data: Patient):
    #patient_data['id'] = UUID 
    #patient = Patient(**patient_data)
    database.append(patient_data.model_dump())
    print (patient_data.model_dump())
    return patient_data

# Read-operatie
def get_patient_by_id(patient_id: str) -> Patient:
    for patient_data in database:
        if patient_data['id'] == UUID(patient_id):
            return Patient(**patient_data)
    return None

# Update-operatie
def update_patient(patient_id: str, patient_data: Patient):
    for i in database:
        if i['id'] == UUID(patient_id):
            index = database.index(i)           
            database[index] = patient_data.model_dump()
            print (database[index])
            return patient_data
    return None

# Delete-operatie
def delete_patient(patient_id: str) -> bool:
    for i, patient_data in enumerate(database):
        if patient_data['id'] == UUID(patient_id):
            del database[i]
            return True
    return False
