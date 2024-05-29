from pydantic import BaseModel, PastDate, UUID5

class ResultaatBase(BaseModel):
    id: UUID5
    onderzoek: None  # dit vervangen met onderzoek class
    naam: str
    datum: PastDate
    omschrijving: str