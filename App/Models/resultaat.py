from pydantic import BaseModel

class ResultaatIn(BaseModel):
    # onderzoek: None  # dit vervangen met onderzoek class
    name: str
    date: str
    discription: str

class ResultaatDb(ResultaatIn):
    id: int