import os
import cryptography
from cryptography.fernet import Fernet
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Password Manager")

# Encryption Key setup
KEY_FILE = "secret.key"
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as kf:
        kf.write(key)
else:
    with open(KEY_FILE, "rb") as kf:
        key = kf.read()

fernet = Fernet(key)
passwords_db = {}

@app.post("/save-password")
def save_password(service: str, password: str):
    if not service or not password:
        raise HTTPException(status_code=400, detail="Invalid data")
    encrypted = fernet.encrypt(password.encode()).decode()
    passwords_db[service] = encrypted
    return {"status": "saved", "service": service}

@app.get("/get-password")
def get_password(service: str):
    if service not in passwords_db:
        raise HTTPException(status_code=404, detail="Service not found")
    decrypted = fernet.decrypt(passwords_db[service].encode()).decode()
    return {"service": service, "password": decrypted}
