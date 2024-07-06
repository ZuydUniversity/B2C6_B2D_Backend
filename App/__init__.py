from .Routes import resultaat, spiersterkte
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .Data import DatabaseModels
from .Data.Database import engine


def initializeApp():
    origins = ["*"]

    DatabaseModels.Base.metadata.create_all(bind=engine)

    app = FastAPI()

    app.include_router(resultaat.router)
    app.include_router(spiersterkte.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    return app
