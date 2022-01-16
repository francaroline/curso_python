from fastapi import FastAPI

app = FastAPI()

@app.get("/status_servidor")
def status_servidor():
    return { "online": True }

@app.get("/")
def root():
    return {"Online e Roteando!"}
