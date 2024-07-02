from pydantic import BaseModel
from .resultaat import ResultaatDb

class SpiersterkteBase(BaseModel):
    spiernaam: str
    spiermyometrie: str
    
class SpiersterkteIn(SpiersterkteBase):
    resultaat_id: int

class SpiersterkteDb(SpiersterkteBase):
    id: int
    resultaat_id: int
    
class SpiersterkteOut(SpiersterkteBase):
    id: int