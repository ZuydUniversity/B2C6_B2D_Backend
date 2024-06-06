from fastapi import FastAPI
from .Routes import ZorgverlenerRoute
from fastapi.middleware.cors import CORSMiddleware

def initializeApp():
    origins = ["*"]
    app = FastAPI()

    app.include_router(ZorgverlenerRoute.router)
    
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
    
    return app