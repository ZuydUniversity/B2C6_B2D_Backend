from pydantic import BaseModel

class Verslag(BaseModel):
    id : int | None = None 
    date: str
    healthcomplaints: str
    medicalhistory: str
    diagnose: str