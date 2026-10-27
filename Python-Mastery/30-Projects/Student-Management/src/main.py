from fastapi import FastAPI

app = FastAPI(title="Student Management")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Student Management"}
