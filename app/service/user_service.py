from typing import Optional, Dict, Any, List
from app.repository.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def create_user(self, name: str, email: str) -> Dict[str, Any]:
        user_id = self.user_repository.create_user(name.strip(), email.lower())
        created_user = self.user_repository.get_user_by_id(user_id)
        return created_user
    
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        return self.user_repository.get_user_by_email(email.lower())
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        return self.user_repository.get_user_by_id(user_id)
    
    def get_all_users(self) -> List[Dict[str, Any]]:
        return self.user_repository.get_all_users()
    
    def update_user(self, user_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Dict[str, Any]:
        updated_user = self.user_repository.get_user_by_id(user_id)
        return updated_user
    
    def delete_user_by_email(self, email: str) -> bool:
        return self.user_repository.delete_user_by_email(email.lower())

    def delete_user_by_id(self, user_id: int) -> bool:
        return self.user_repository.delete_user_by_id(user_id)
