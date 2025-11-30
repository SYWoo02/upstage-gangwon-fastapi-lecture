from fastapi import HTTPException

from app.core.db import SessionLocal
from app.models.users import User
from typing import Optional, Dict, Any, List
from sqlalchemy.orm import Session


class UserRepository:
    
    def create_user(self, name: str, email: str) -> int:
        db: Session = SessionLocal()
        try:
            user = User(name=name, email=email)
            db.add(user)
            db.commit()
            db.refresh(user)
            return user.id
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal server error")

        finally:
            db.close()

    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        db: Session = SessionLocal()
        try:
            user = db.query(User).filter(User.email == email).first()
            if user:
                return {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "created_at": user.created_at
                }
            return None
        finally:
            db.close()


    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        db: Session = SessionLocal()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if user:
                return {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "created_at": user.created_at
                }
            return None
        finally:
            db.close()


    def get_all_users(self) -> List[Dict[str, Any]]:
        db: Session = SessionLocal()
        try:
            users = db.query(User).order_by(User.created_at.desc()).all()
            return [
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "created_at": user.created_at
                }
                for user in users
            ]
        finally:
            db.close()


    def update_user(self, user_id: int, **kwargs) -> bool:
        if not kwargs:
            return True
            
        db: Session = SessionLocal()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                return False
                
            updated = False
            for key, value in kwargs.items():
                if value is not None and key in ['name', 'email']:
                    setattr(user, key, value)
                    updated = True
                    
            if updated:
                db.commit()
                
            return updated
        finally:
            db.close()


    def delete_user_by_email(self, email: str) -> bool:
        db: Session = SessionLocal()
        try:
            user = db.query(User).filter(User.email == email).first()
            if user:
                db.delete(user)
                db.commit()
                return True
            return False
        finally:
            db.close()


    def delete_user_by_id(self, user_id: int) -> bool:
        db: Session = SessionLocal()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if user:
                db.delete(user)
                db.commit()
                return True
            return False
        finally:
            db.close()


    def user_exists_by_email(self, email: str) -> bool:
        db: Session = SessionLocal()
        try:
            return db.query(User).filter(User.email == email).first() is not None
        finally:
            db.close()

