from fastapi import FastAPI

app = FastAPI(title="AI Chatbot")

@app.get("/")
def read_root():
    return {"status": "running", "project": "AI Chatbot"}
