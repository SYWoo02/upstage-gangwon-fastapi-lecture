from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from app.service.chat_service import ChatService
from app.dependencies import get_chat_service

router = APIRouter(prefix="/chat", tags=["chat"])


class MessageCreate(BaseModel):
    user_id: int
    message: str


class ChatTransaction(BaseModel):
    user_id: int
    user_message: str
    assistant_message: str


class ConversationResponse(BaseModel):
    id: int
    user_id: int
    role: str
    message: str
    created_at: str


@router.post("/user-message")
async def add_user_message_api(
    message_data: MessageCreate,
    chat_service: ChatService = Depends(get_chat_service)
):
    try:
        chat_service.add_user_message(message_data.user_id, message_data.message)
        return {"message": "User message added successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/assistant-message")
async def add_assistant_message_api(
    message_data: MessageCreate,
    chat_service: ChatService = Depends(get_chat_service)
):
    try:
        chat_service.add_assistant_message(message_data.user_id, message_data.message)
        return {"message": "Assistant message added successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{user_id}/conversations", response_model=List[ConversationResponse])
async def get_conversations_api(
    user_id: int, 
    limit: int = 20,
    chat_service: ChatService = Depends(get_chat_service)
):
    try:
        conversations = chat_service.get_recent_conversations(user_id, limit)
        return conversations or []
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/transaction")
async def save_chat_transaction_api(
    transaction: ChatTransaction,
    chat_service: ChatService = Depends(get_chat_service)
):
    try:
        chat_service.save_chat_transaction(
            transaction.user_id,
            transaction.user_message,
            transaction.assistant_message
        )
        return {"message": "Chat transaction saved successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")