from fastapi import FastAPI

app = FastAPI(title="Chat App")

@app.get("/")
def read_root():
    return {"status": "running", "project": "Chat App"}
