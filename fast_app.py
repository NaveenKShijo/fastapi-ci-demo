from fastapi import FastAPI

app = FastAPI()

@app.get("/home/")
def get_home():
    return {"response": "Welcome here at home"}
