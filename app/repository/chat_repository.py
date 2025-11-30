from app.core.db import SessionLocal
from app.models.conversation import Conversation
from app.models.role import Role
from typing import List, Dict, Any
from sqlalchemy.orm import Session


class ChatRepository:
    
    def add_conversation(self, user_id: int, role: str, message: str) -> None:
        db: Session = SessionLocal()
        try:
            conversation = Conversation(
                user_id=user_id,
                role=Role(role),
                message=message
            )
            db.add(conversation)
            db.commit()
        finally:
            db.close()


    def get_recent_conversations(self, user_id: int, limit: int = 20) -> List[Dict[str, Any]]:
        db: Session = SessionLocal()
        try:
            conversations = db.query(Conversation).filter(
                Conversation.user_id == user_id
            ).order_by(Conversation.created_at.desc()).limit(limit).all()
            
            return [
                {
                    "id": conv.id,
                    "user_id": conv.user_id,
                    "role": conv.role.value,
                    "message": conv.message,
                    "created_at": conv.created_at
                }
                for conv in conversations
            ]
        finally:
            db.close()


    def save_chat_transaction(self, user_id: int, user_msg: str, assistant_msg: str) -> None:
        db: Session = SessionLocal()
        try:
            # 1) 사용자 메시지 저장
            user_conversation = Conversation(
                user_id=user_id,
                role=Role.user,
                message=user_msg
            )
            db.add(user_conversation)
            
            # 2) 어시스턴트 메시지 저장
            assistant_conversation = Conversation(
                user_id=user_id,
                role=Role.assistant,
                message=assistant_msg
            )
            db.add(assistant_conversation)
            
            db.commit()  # 두 개가 모두 성공한 경우에만 commit

        except Exception as e:
            db.rollback()  # 하나라도 실패하면 전체 취소
            raise e
        finally:
            db.close()


    def save_chat_transaction_fail(self, user_id: int, user_msg: str, assistant_msg: str) -> None:
        db: Session = SessionLocal()
        try:
            # 1) 사용자 메시지 저장
            user_conversation = Conversation(
                user_id=user_id,
                role=Role.user,
                message=user_msg
            )
            db.add(user_conversation)
            
            # 2) 어시스턴트 메시지 저장
            assistant_conversation = Conversation(
                user_id=user_id,
                role=Role.assistant,
                message=assistant_msg
            )
            db.add(assistant_conversation)
            
            db.commit()  # 두 개가 모두 성공한 경우에만 commit

        except Exception as e:
            db.rollback()  # 하나라도 실패하면 전체 취소
            raise e
        finally:
            db.close()

