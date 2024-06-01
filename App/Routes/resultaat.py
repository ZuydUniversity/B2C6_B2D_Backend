from fastapi import APIRouter
from uuid import UUID

from App.Models.resultaat import ResultaatBase
from App.Services.dal import resultaat_get_by_id, resultaat_update_by_id


router = APIRouter()

@router.get("/resultaat/{id}", response_model=ResultaatBase)
async def get_resultaat(user_id: UUID):
    return resultaat_get_by_id(user_id)

@router.put("/resultaat/{id}", response_model=ResultaatBase)
async def update_resultaat(id: UUID, update_data: ResultaatBase):
    resultaat = resultaat_update_by_id(id, update_data)
    return resultaat