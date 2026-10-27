from fastapi import FastAPI

app = FastAPI(title="Calculator")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Calculator"}
