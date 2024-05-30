from App import initializeApp

app = initializeApp()

@app.get("/")
async def root():
    return {"data": "Hello Wolrd"}