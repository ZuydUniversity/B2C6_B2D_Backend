from fastapi import FastAPI
from .Routes import ZorgverlenerRoute
from fastapi.middleware.cors import CORSMiddleware

def initializeApp():
    origins = ["52.166.135.125", "*", "127.0.0.1"]
    app = FastAPI()
    app.include_router(ZorgverlenerRoute.router)
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)
    return app