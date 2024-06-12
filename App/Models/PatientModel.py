from pydantic import BaseModel

class Patient(BaseModel):
    id: int | None = None
    name: str
    address: str
    postalZip: str
    phone: str
    email: str
    