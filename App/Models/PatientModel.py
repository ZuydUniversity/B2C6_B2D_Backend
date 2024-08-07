from pydantic import BaseModel

class Patient(BaseModel):
    id: int;
    name: str;
    surname: str;
    age: int;
    gender: str;
    address: str;
    city: str;
    email: str;
    diagnosis: str;
    medication: str;
    phonenumber: int;
