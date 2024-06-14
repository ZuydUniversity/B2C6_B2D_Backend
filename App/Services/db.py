from uuid import UUID


def resultaat_get_data_by_id(user_id: UUID) -> ...:
    # db conn??

    return ...

def resultaat_update_data_by_id(user_id: UUID, update_data: dict):
    if user_id in ...:
        ...[user_id] = update_data