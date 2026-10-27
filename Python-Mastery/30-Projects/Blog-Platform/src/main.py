from fastapi import FastAPI

app = FastAPI(title="Blog Platform")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Blog Platform"}
