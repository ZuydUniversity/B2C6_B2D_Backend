from uuid import UUID

from App.Models.resultaat import ResultaatBase
from App.Services.db import resultaat_get_data_by_id, resultaat_update_data_by_id

def resultaat_get_by_id(user_id: UUID) -> ResultaatBase:
    RESULTAAT_DATA = resultaat_get_data_by_id(user_id)
    RESULTAAT: ResultaatBase = ...

    return RESULTAAT

def resultaat_update_by_id(user_id: UUID, update_data: ResultaatBase) -> ResultaatBase:
    existing_resultaat = resultaat_get_data_by_id(user_id)
    if not existing_resultaat:
        return None
    
    update_fields = update_data.dict(exclude_unset=True)
    updated_resultaat_data = {**existing_resultaat, **update_fields}
    resultaat_update_data_by_id(user_id, updated_resultaat_data)
    
    updated_resultaat = ResultaatBase(**updated_resultaat_data)
    return updated_resultaat