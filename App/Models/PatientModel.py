from pydantic import BaseModel

class Patient(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int
    address: str
    housenumber: str
    city: str
    telephonenumber: int