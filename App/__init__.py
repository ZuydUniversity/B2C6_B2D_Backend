from fastapi import FastAPI

from App.Routes.resultaat import router as resultaat_router

def initializeApp():
    app = FastAPI()
    app.include_router(resultaat_router)

    return app