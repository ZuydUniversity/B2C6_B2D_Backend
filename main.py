from App import initializeApp
#from App.Models.Patient import Patient
#from App.Routes.Patient_Router import Patient_Router
app = initializeApp()

# app.include_router(Patient_Router.router)


# database = []

# @app.get('/patients')
# async def GetPatients():
#     return { "data" : "This is the GetPatients!"}

# @app.get("/patient/{id}")
# def get_patient(id):
#     print(id)
#     return {"patient_detail": f"Hier is patiënt {id}"}



# @app.post('/patients')
# def create_patients(patient: Patient):
#     print(patient)
#     print(patient.model.dump())
#     return {"data": patient}


# @app.delete('/patients')
# async def deletePatients():
#     return { "data" : "hoi123"}

# @app.put('/patients')
# async def updatePatients():
#     return { "data" : "hoi123"}