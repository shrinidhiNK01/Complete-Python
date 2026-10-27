from fastapi import FastAPI

app = FastAPI(title="Banking System")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Banking System"}
