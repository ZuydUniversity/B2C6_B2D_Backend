from pydantic import BaseModel, PastDate, UUID5

class Resultaat(BaseModel):
    #id: UUID5
    id: int | None = None
    onderzoek: None  # dit vervangen met onderzoek class
    name: str
    date: PastDate
    discription: str