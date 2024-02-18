import redis
import json
from uuid import uuid4

# Initialize the Redis client with a connection pool
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

def start_chat_session() -> str:
    """
    Starts a new chat session by generating a unique session token
    and initializing an empty chat history in Redis.
    
    Returns:
        session_token (str): A unique token for the session.
    """
    session_token = str(uuid4())
    r.set(session_token, json.dumps([]))
    return session_token

def save_message_to_history(session_token: str, role: str, content: str):
    """
    Saves a message to the chat history for a given session token.
    
    Parameters:
        session_token (str): The session token identifying the chat session.
        role (str): The role of the message sender (e.g., "user", "assistant").
        content (str): The content of the message.
    """
    if r.exists(session_token):
        chat_history = json.loads(r.get(session_token) or '[]')
        chat_history.append({"role": role, "content": content})
        r.set(session_token, json.dumps(chat_history))

def get_chat_history(session_token: str) -> list:
    """
    Retrieves the chat history for a given session token.
    
    Parameters:
        session_token (str): The session token identifying the chat session.
    
    Returns:
        chat_history (list): The chat history as a list of message dictionaries.
    """
    if r.exists(session_token):
        return json.loads(r.get(session_token) or '[]')
    return []

def session_exists(session_token: str) -> bool:
    """
    Checks if a session exists for the given token.
    
    Parameters:
        session_token (str): The session token to check.
    
    Returns:
        exists (bool): True if the session exists, False otherwise.
    """
    return r.exists(session_token)
