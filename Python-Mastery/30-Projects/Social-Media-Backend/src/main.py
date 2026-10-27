from fastapi import FastAPI

app = FastAPI(title="Social Media Backend")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Social Media Backend"}
