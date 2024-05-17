from fastapi import FastAPI
from models import Person
from database import Sessionlocal

app = FastAPI() # standaard webserver runnen met uvicorn --> uvicorn main:app --reload


@app.get("/")
def read_root():
    return "hello world"

if __name__ == "__main__": # eerst je database opzetten en dan runnen met python main.py
    db = Sessionlocal()
    person = Person(name="hoi", gender="test")
    db.add(person)
    db.commit()
    db.close()


# @app.get("/persons")
# hier moet je de database gegevens ophalen met een query get all 


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}