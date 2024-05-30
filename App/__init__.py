from fastapi import FastAPI
from .Routes import ZorgverlenerRoute

def initializeApp():
    app = FastAPI()
    app.include_router(ZorgverlenerRoute.router)
    return app