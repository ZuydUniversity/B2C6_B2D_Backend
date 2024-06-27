from App.Models.ZorgverlenerModel import Zorgverlener
from .testDatabase import client, session
import pytest

@pytest.fixture
def createZorgverlener():
    return {"id": 1,
            "name": "Dorra",
            "lastName": "Van de Buurt",
            "email": "dorra@OpDeKaart.click",
            "phoneNumber": "0600000000",
            "password": "Is een geheim",
            "profession": "Explorer",
            "isActive": True}

    
def test_create_zorgverlener(client,createZorgverlener):
    response = client.post("/zorgverleners",json=createZorgverlener)
    assert response.status_code == 200
    assert response.json() == f'New Zorgverlener with id:{createZorgverlener['id']} created!'


def test_get_zorgverleners(client,createZorgverlener):
    client.post("/zorgverleners",json=createZorgverlener)
    response = client.get(f"/zorgverleners")
    assert response.status_code == 200
    assert response.json() == [createZorgverlener]

def test_get_zorgverlener_by_id(client,createZorgverlener):
    client.post("/zorgverleners",json=createZorgverlener)
    response = client.get(f"/zorgverleners/{createZorgverlener['id']}")
    assert response.status_code == 200
    assert response.json() == createZorgverlener

def test_update_zorgverlener(client,createZorgverlener):
    client.post("/zorgverleners",json=createZorgverlener)
    createZorgverlener["password"] = "Nog steeds een geheim!"
    response = client.put(f"/zorgverleners/{createZorgverlener.get("id")}"
                          ,json=createZorgverlener)
    assert response.status_code == 200
    assert response.json() == createZorgverlener

def test_delete_zorgverlener(client,createZorgverlener):
    client.post("/zorgverleners",json=createZorgverlener)
    response = client.delete(f"/zorgverleners/{createZorgverlener.get("id")}")
    assert response.status_code == 200
    assert response.json() == f'Zorgverlener with id:{createZorgverlener['id']} has been removed succesfuly!'