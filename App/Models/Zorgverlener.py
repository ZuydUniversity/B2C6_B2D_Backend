from pydantic import BaseModel


class Zorgverlener(BaseModel):
    id: int
    naam: str
    achternaam: str
    email: str
    wachtwoord: str
    