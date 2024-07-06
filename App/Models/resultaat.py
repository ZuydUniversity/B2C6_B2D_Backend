from pydantic import BaseModel
from .spiersterkte import SpiersterkteOut


class ResultaatBase(BaseModel):
    # onderzoek: None  # dit vervangen met onderzoek class
    name: str
    date: str
    discription: str


class ResultaatIn(ResultaatBase):
    ...


class ResultaatDb(ResultaatBase):
    id: int

    
class ResultaatOut(ResultaatBase):
    id: int
    spiersterkten: list[SpiersterkteOut]
