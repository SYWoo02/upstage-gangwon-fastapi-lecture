from typing import List, Dict, Any
from app.models.role import Role
from app.repository.chat_repository import ChatRepository


class ChatService:
    def __init__(self, chat_repository: ChatRepository):
        self.chat_repository = chat_repository
    
    def add_user_message(self, user_id: int, message: str) -> None:
        if user_id <= 0:
            raise ValueError("User ID must be positive")
        if not message or not message.strip():
            raise ValueError("Message cannot be empty")
            
        self.chat_repository.add_conversation(user_id, Role.user.name, message.strip())
    
    def add_assistant_message(self, user_id: int, message: str) -> None:
        if user_id <= 0:
            raise ValueError("User ID must be positive")
        if not message or not message.strip():
            raise ValueError("Message cannot be empty")
            
        self.chat_repository.add_conversation(user_id, Role.assistant.name, message.strip())
    
    def get_recent_conversations(self, user_id: int, limit: int = 20) -> List[Dict[str, Any]]:
        if user_id <= 0:
            raise ValueError("User ID must be positive")
        if limit <= 0 or limit > 100:
            raise ValueError("Limit must be between 1 and 100")
            
        return self.chat_repository.get_recent_conversations(user_id, limit)
    
    def save_chat_transaction(self, user_id: int, user_msg: str, assistant_msg: str) -> None:
        if user_id <= 0:
            raise ValueError("User ID must be positive")
        if not user_msg or not user_msg.strip():
            raise ValueError("User message cannot be empty")
        if not assistant_msg or not assistant_msg.strip():
            raise ValueError("Assistant message cannot be empty")
            
        self.chat_repository.save_chat_transaction(user_id, user_msg.strip(), assistant_msg.strip())
    
    def save_chat_transaction_fail(self, user_id: int, user_msg: str, assistant_msg: str) -> None:
        if user_id <= 0:
            raise ValueError("User ID must be positive")
        if not user_msg or not user_msg.strip():
            raise ValueError("User message cannot be empty")
        if not assistant_msg or not assistant_msg.strip():
            raise ValueError("Assistant message cannot be empty")
            
        self.chat_repository.save_chat_transaction_fail(user_id, user_msg.strip(), assistant_msg.strip())
