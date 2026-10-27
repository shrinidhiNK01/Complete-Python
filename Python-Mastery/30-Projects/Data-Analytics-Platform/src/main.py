from fastapi import FastAPI

app = FastAPI(title="Data Analytics Platform")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Data Analytics Platform"}
