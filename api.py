from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from cryptography.fernet import Fernet, InvalidToken
import jwt
from jwt.exceptions import InvalidTokenError
import ucip_pb2  # Compiled Protobuf
from google.protobuf.json_format import MessageToJson, Parse
import uvicorn
import logging

app = FastAPI(title="UCIP API")
security = HTTPBearer()

# Demo secrets (replace in production)
ENCRYPTION_KEY = Fernet.generate_key()  # Or load from env
JWT_SECRET = "your_jwt_secret"
fernet = Fernet(ENCRYPTION_KEY)

# In-memory DB (replace with encrypted DB)
user_contexts = {}  # {user_id: encrypted_binary}

logging.basicConfig(level=logging.INFO)

def decode_jwt(token: str):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except InvalidTokenError:
        raise HTTPException(401, "Invalid token")

@app.get("/getContext/{user_id}")
def get_context(user_id: str, credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = decode_jwt(credentials.credentials)
    if user_id != payload.get("user_id"):
        raise HTTPException(403, "Unauthorized")
    
    if user_id not in user_contexts:
        raise HTTPException(404, "Not found")
    
    encrypted_data = user_contexts[user_id]
    try:
        decrypted = fernet.decrypt(encrypted_data)
        ucip = ucip_pb2.UCIP()
        ucip.ParseFromString(decrypted)
        logging.info(f"Accessed UCIP for {user_id}")
        return {"data": MessageToJson(ucip)}  # Return JSON for LLM compatibility
    except InvalidToken:
        raise HTTPException(400, "Decryption failed")

@app.post("/updateContext/{user_id}")
def update_context(user_id: str, data: dict, credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = decode_jwt(credentials.credentials)
    if user_id != payload.get("user_id"):
        raise HTTPException(403, "Unauthorized")
    
    # Validate consent and scopes (example)
    if not data.get("consent", {}).get("granted"):
        raise HTTPException(400, "Consent required")
    
    ucip = ucip_pb2.UCIP()
    Parse(MessageToJson(data), ucip)  # From JSON to Protobuf (for input flexibility)
    binary = ucip.SerializeToString()
    encrypted = fernet.encrypt(binary)
    user_contexts[user_id] = encrypted
    logging.info(f"Updated UCIP for {user_id}")
    return {"message": "Updated"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
