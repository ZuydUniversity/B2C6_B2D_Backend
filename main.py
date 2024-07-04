from fastapi import FastAPI
from App.Routes import PatientRoute

app = FastAPI()

app.include_router(PatientRoute.router)
