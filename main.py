from App import initializeApp

app = initializeApp()

@app.get("/")
def read_root():
    return {"Hello": "World"}