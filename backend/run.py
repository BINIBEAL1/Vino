# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Vino Bingo backend running!"}
