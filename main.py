from App import initializeApp

app = initializeApp()
@app.get("/")
dev root ():
    return {
        "data": "fabian moment"
    }