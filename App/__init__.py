from App.Data import DatabaseModels
from App.Data.Database import engine
from App.Routes import resultaat, spiersterkte
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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
