from pydantic import BaseModel
from uuid import UUID 

class Patient(BaseModel):
    id: UUID
    name: str
    surname: str
    email: str
    age: int
    address: str
    housenumber: str
    city: str
    telephonenumber: int

    


