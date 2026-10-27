from fastapi import FastAPI

app = FastAPI(title="Enterprise SaaS Backend")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Enterprise SaaS Backend"}
