from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.conversation import Conversation

class ConversationService:

    def crear_conversacion(self, db: Session) -> Conversation:

        conversacion = Conversation()

        db.add(conversacion)
        db.commit()
        db.refresh(conversacion)

        return conversacion
    
    def obtener_o_crear_conversacion(self, db: Session) -> Conversation:
        conversacion = db.scalar(
            select(Conversation)
        )

        if conversacion:
            return conversacion

        return self.crear_conversacion(db)