from Database import DataAccessLayer
from PersonClass import Person
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return{'hello': 'again'}

@app.get('/person')
def get_persons():
    Database = DataAccessLayer()
    return Database.get_persons()

@app.post('/persons')
def create_person(person_name : str):
    Database = DataAccessLayer()
    