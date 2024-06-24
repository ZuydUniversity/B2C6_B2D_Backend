# from App import initializeApp

# app = initializeApp()

from fastapi import FastAPI
from PersonClass import Person

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
