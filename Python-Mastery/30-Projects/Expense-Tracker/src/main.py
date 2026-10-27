from fastapi import FastAPI

app = FastAPI(title="Expense Tracker")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Expense Tracker"}
