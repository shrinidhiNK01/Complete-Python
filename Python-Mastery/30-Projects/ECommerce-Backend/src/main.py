from fastapi import FastAPI

app = FastAPI(title="ECommerce Backend")

@app.get("/")
def read_root():
    return {"status": "running", "project": "ECommerce Backend"}
