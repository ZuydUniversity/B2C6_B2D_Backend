from uuid import UUID


def resultaat_get_data_by_id(user_id: UUID) -> ...:
    # db conn??
    
    return ...
    
def resultaat_delete_data_by_id(user_id: UUID) -> None:
    if user_id in ...:
        del ...[user_id]
    else:
        raise KeyError("Resultaat niet gevonden")