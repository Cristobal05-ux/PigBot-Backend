from app.database.database import SessionLocal

from app.services.audio_service import AudioService
from app.services.chat_service import ChatService


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_chat_service() -> ChatService:
    return ChatService()


def get_audio_service() -> AudioService:
    return AudioService()