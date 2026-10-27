from fastapi import FastAPI

app = FastAPI(title="Video Processing")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Video Processing"}
