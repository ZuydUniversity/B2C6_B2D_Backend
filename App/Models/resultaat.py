from pydantic import BaseModel
from .spiersterkte import SpiersterkteOut

class ResultaatIn(BaseModel):
    # onderzoek: None  # dit vervangen met onderzoek class
    name: str
    date: str
    discription: str

class ResultaatDb(ResultaatIn):
    id: int
    
class ResultaatOut(ResultaatIn):
    spiersterkten: tuple[SpiersterkteOut]