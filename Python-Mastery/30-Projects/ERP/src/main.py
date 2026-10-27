from fastapi import FastAPI

app = FastAPI(title="ERP")

@app.get("/")
def read_root():
    return {"status": "running", "project": "ERP"}
