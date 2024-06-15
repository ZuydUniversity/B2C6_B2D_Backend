from fastapi import FastAPI
from .Routes import PatientRoute

app = FastAPI()

app.include_router(PatientRoute.router)
