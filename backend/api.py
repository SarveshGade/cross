from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"Hello" : "World"}

@app.get("/app/puzzle")
def get_puzzle():
    return {"Hello" : "World"}

