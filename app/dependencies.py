from fastapi import Depends
from app.repository.user_repository import UserRepository
from app.repository.chat_repository import ChatRepository
from app.service.user_service import UserService
from app.service.chat_service import ChatService


def get_user_repository() -> UserRepository:
    return UserRepository()


def get_chat_repository() -> ChatRepository:
    return ChatRepository()


def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository)
) -> UserService:
    return UserService(user_repository)


def get_chat_service(
    chat_repository: ChatRepository = Depends(get_chat_repository)
) -> ChatService:
    return ChatService(chat_repository)