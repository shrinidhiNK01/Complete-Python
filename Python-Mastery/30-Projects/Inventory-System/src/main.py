from fastapi import FastAPI

app = FastAPI(title="Inventory System")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Inventory System"}
