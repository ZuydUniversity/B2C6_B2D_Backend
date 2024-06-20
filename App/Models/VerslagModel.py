
from pydantic import BaseModel

class Verslag(BaseModel):
    id: int | None = None
    date: str
    healthcomplaints: str
    medicalhistory: str
    diagnose: str


# from sqlalchemy import Column, Integer, String
# from App.Data.Database import Base  # Zorg ervoor dat je Base van de juiste plaats importeert

# class Verslag(Base):
#     __tablename__ = "verslagen1"

#     id = Column(Integer, primary_key=True, index=True)
#     date = Column(String(100), index=True)
#     healthcomplaints = Column(String(500), index=True)
#     medicalhistory = Column(String(500), index=True)
#     diagnose = Column(String(100), index=True)
