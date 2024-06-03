from App import initializeApp

app = initializeApp()

@app.get("/")
def root():
    return{"Data": "Hello World"}