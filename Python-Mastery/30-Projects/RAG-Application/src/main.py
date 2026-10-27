from fastapi import FastAPI

app = FastAPI(title="RAG Application")

@app.get("/")
def read_root():
    return {"status": "running", "project": "RAG Application"}
