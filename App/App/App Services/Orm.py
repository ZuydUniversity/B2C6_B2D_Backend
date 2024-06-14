from uuid import UUID

from App.Models.resultaat import ResultaatBase
from App.Services.db import resultaat_get_data_by_id

def resultaat_get_by_id(user_id: UUID) -> ResultaatBase:
    RESULTAAT_DATA = resultaat_get_data_by_id(user_id)
    RESULTAAT: ResultaatBase = ...
    
    return RESULTAAT

def resultaat_delete_by_id(user_id: UUID) -> None:
    existing_resultaat = resultaat_get_data_by_id(user_id)
    if not existing_resultaat:
        return None
    
    resultaat_delete_data_by_id(user_id)
