from fastapi import APIRouter
from ..Models.Zorgverlener import Zorgverlener

database = [
  {
    "id": 1,
    "naam": "Jan",
    "achternaam": "de Vries",
    "email": "jan.de vries@voorbeeld.com",
    "wachtwoord": "wachtwoord1"
  },
  {
    "id": 2,
    "naam": "Piet",
    "achternaam": "Jansen",
    "email": "piet.jansen@voorbeeld.com",
    "wachtwoord": "wachtwoord2"
  },
  {
    "id": 3,
    "naam": "Klaas",
    "achternaam": "Bakker",
    "email": "klaas.bakker@voorbeeld.com",
    "wachtwoord": "wachtwoord3"
  },
  {
    "id": 4,
    "naam": "Els",
    "achternaam": "Visser",
    "email": "els.visser@voorbeeld.com",
    "wachtwoord": "wachtwoord4"
  },
  {
    "id": 5,
    "naam": "Anne",
    "achternaam": "Smit",
    "email": "anne.smit@voorbeeld.com",
    "wachtwoord": "wachtwoord5"
  },
  {
    "id": 6,
    "naam": "Lisa",
    "achternaam": "Meijer",
    "email": "lisa.meijer@voorbeeld.com",
    "wachtwoord": "wachtwoord6"
  },
  {
    "id": 7,
    "naam": "Sander",
    "achternaam": "Mulder",
    "email": "sander.mulder@voorbeeld.com",
    "wachtwoord": "wachtwoord7"
  },
  {
    "id": 8,
    "naam": "Emma",
    "achternaam": "de Jong",
    "email": "emma.de jong@voorbeeld.com",
    "wachtwoord": "wachtwoord8"
  },
  {
    "id": 9,
    "naam": "Tom",
    "achternaam": "Bos",
    "email": "tom.bos@voorbeeld.com",
    "wachtwoord": "wachtwoord9"
  },
  {
    "id": 10,
    "naam": "Lotte",
    "achternaam": "van Dijk",
    "email": "lotte.van dijk@voorbeeld.com",
    "wachtwoord": "wachtwoord10"
  }
]


router = APIRouter(
    prefix="/zorgverleners"
)

@router.get("/")
async def get_zorgverleners():
    return {"data": database}

@router.get("/{id}")
async def get_zorgverlenerById(id: int):
    for z in database:
        if z["id"] == id:

            return z

@router.post("/")
async def add_zorgverlener(zorgverlener: Zorgverlener):

    database.append(zorgverlener.model_dump())

    return zorgverlener


@router.delete("/{id}")
async def delete_zorgverlener(id: int):

    deletedzorgverlener = None
    for z in database:
        if z["id"] == id:
            index = database.index(z)
            deletedzorgverlener = database.pop(index)
    return {"Deleted object" : deletedzorgverlener}