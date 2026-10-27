from fastapi import FastAPI

app = FastAPI(title="ETL Pipeline")

@app.get("/")
def read_root():
    return {"status": "running", "project": "ETL Pipeline"}
