# from fastapi import FastAPI
# from .Routes import PatientRouter

# def initializeApp():
#     app = FastAPI()
#     app.include_router(PatientRouter.router)
#     return app


from fastapi import FastAPI
from .Routes import PatientRouter
from fastapi.middleware.cors import CORSMiddleware
from .Data import DatabaseModels
from App.Data.Database import engine
from .Routes import ZorgverlenerRoute
from .Routes import VerslagRoute
from fastapi.middleware.cors import CORSMiddleware
from .Data import DatabaseModels
from .Data.Database import engine


from .Routes import Patient_Router

def initializeApp():
    origins = ["*"]

    DatabaseModels.Base.metadata.create_all(bind=engine)

    app = FastAPI()

    app.include_router(PatientRouter.router)
    app.include_router(ZorgverlenerRoute.router)
    app.include_router(VerslagRoute.router)
    app.include_router(Patient_Router.router)
    
    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
    
    
    return app