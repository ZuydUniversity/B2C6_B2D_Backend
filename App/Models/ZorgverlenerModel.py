from pydantic import BaseModel

class Zorgverlener(BaseModel):
    id: int | None = None
    name: str
    lastName: str
    email: str
    phoneNumber: int
    password: str
    profession: str
    