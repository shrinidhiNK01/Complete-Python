from fastapi import FastAPI

app = FastAPI(title="Recommendation Engine")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Recommendation Engine"}
