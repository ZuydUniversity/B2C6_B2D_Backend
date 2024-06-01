from fastapi import FastAPI
from .Routes import Patient_Router

def initializeApp():
    app = FastAPI()
    app.include_router(Patient_Router.router)
    return app