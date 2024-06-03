from App import initializeApp

app = initializeApp()
@app.get("/")
def root ():
    return {
        "data": "fabian moment"
    }