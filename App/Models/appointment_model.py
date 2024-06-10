from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Appointment(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    location: str
    department: str
    date: datetime    