from fastapi import APIRouter
from uuid import UUID

from App.Models.resultaat import ResultaatBase
from App.Services.dal import resultaat_get_by_id
from App.Services.dal import resultaat_delete_by_id


router = APIRouter()

@router.get("/resultaat/{id}", response_model=ResultaatBase)
async def get_resultaat(user_id: UUID):
    return resultaat_get_by_id(user_id)

@router.post("/items?{item_id}")
async def Create_Resultaat(resultaat: ResultaatBase):
    return {"resultaat_name": resultaat.naam,"Resultaat_date": resultaat.datum,"resultaat_discription": resultaat.omschrijving}


@router.delete("/resultaat/{id}", response_model=dict)
async def delete_resultaat(id: UUID):
    resultaat_delete_by_id(id)  
    return {"detail": "Resultaat is met succes verwijderd"}