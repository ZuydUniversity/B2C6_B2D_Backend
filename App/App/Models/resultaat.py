from pydantic import BaseModel, PastDate

class ResultaatBase(BaseModel):
    onderzoek: None  # dit vervangen met onderzoek class
    naam: str
    datum: PastDate
    omschrijving: str