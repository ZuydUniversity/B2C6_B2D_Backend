from fastapi import FastAPI
from .Routes import ZorgverlenerRoute
from fastapi.middleware.cors import CORSMiddleware

def initializeApp():
    origins = ["http://localhost:80", "https://localhost","http://52.166.135.125:80", "http://localhost:8000", "https://localhost:8000","*"]
    app = FastAPI()
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
    app.include_router(ZorgverlenerRoute.router)
    return app