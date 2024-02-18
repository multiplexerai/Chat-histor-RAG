from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from chat_history_manager import start_chat_session, save_message_to_history, get_chat_history, session_exists

app = FastAPI()
security = HTTPBearer()

# Adjusted endpoints to use the chat_history_manager functions

@app.get("/start_chat")
def start_chat():
    session_token = start_chat_session()
    return {"session_token": session_token}

@app.get("/send_message/{message}")
async def send_message(message: str, session_token: str):
    if not session_exists(session_token):
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )
    # Example usage, adjust according to your application logic
    save_message_to_history(session_token, "user", message)
    # Proceed with your message handling logic
    return {"response": "Message received and saved"}

@app.get("/get_history")
def get_history(token: HTTPAuthorizationCredentials = Depends(security)):
    session_token = token.credentials
    if not session_exists(session_token):
        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )
    chat_history = get_chat_history(session_token)
    return {"history": chat_history}
