from App import initializeApp
from App.Routes.appointment_routes import router as appointment_router

app = initializeApp()
app.include_router(appointment_router)

# Root Endpoint
@app.get("/")
def Root():
    return{"message": "Hello World"}
