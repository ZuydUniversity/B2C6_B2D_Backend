from pydantic import BaseModel, PastDate, UUID

class ResultaatBase(BaseModel):
    id: UUID
    onderzoek: None  # dit vervangen met onderzoek class
    naam: str
    datum: PastDate
    omschrijving: str