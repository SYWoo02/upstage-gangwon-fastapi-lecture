# app/models/conversation.py
from sqlalchemy import Column, Integer, String, DateTime, Enum, func
from app.models.base import Base
from app.models.role import Role  # 기존 enum 그대로 사용


class Conversation(Base):
  __tablename__ = "conversations"

  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, nullable=False)
  role = Column(Enum(Role), nullable=False)  # 'user' / 'assistant'
  message = Column(String(500), nullable=False)
  created_at = Column(DateTime, server_default=func.now())
