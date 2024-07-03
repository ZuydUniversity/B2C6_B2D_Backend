from App.Models.PatientModel import Patient
from App.Data.Database import client, session
import pytest

@pytest.fixture
def createPatient():
    return {"id": 1,
            "name": "Hans",
            "surname": "Joost",
            "age": "18",
            "gender": "Man",
            "address": "Kelinstraat",
            "city": "Kerkrade",
            "email": "Hans@joost.nl",
            "diagnosis": "Buikgriep",
            "medication": "Ibo",
            "phonenumber": "0612345678",}

    
def patient(client,createpatient):
    response = client.post("/zorgverleners",json=createpatient)
    assert response.status_code == 200
    assert response.json() == f'New Patient with id:{createpatient['id']} created!'


def test_get_patient(client,createpatient):
    client.post("/patient",json=createpatient)
    response = client.get(f"/patient")
    assert response.status_code == 200
    assert response.json() == [createpatient]

def test_get_patient_by_id(client,createpatient):
    client.post("/patient",json=createpatient)
    response = client.get(f"/patient/{createpatient['id']}")
    assert response.status_code == 200
    assert response.json() == createpatient

def test_update_patient(client,createpatient):
    client.post("/patient",json=createpatient)
    createpatient["gender"] = "Nog steeds hetzelfde!"
    response = client.put(f"/patient/{createpatient.get("id")}"
                          ,json=createpatient)
    assert response.status_code == 200
    assert response.json() == createpatient

def test_delete_patient(client,createpatient):
    client.post("/patient",json=createpatient)
    response = client.delete(f"/patient/{createpatient.get("id")}")
    assert response.status_code == 200
    assert response.json() == f'patient with id:{createpatient['id']} has been removed succesfuly!'