from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from App.Data import databaseModels
from App.Data.database import engine

def initializeApp():
    
    databaseModels.Base.metadata.create_all(bind=engine)

    app = FastAPI()
    origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://98.71.218.67:8000/",
    "http://98.71.218.67",


    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app







