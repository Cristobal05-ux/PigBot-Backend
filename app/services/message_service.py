from sqlalchemy.orm import Session
from sqlalchemy import select, desc
from app.models.message import Message

class MessageService:

    def guardar_mensaje(
        self,
        db: Session,
        conversation_id: str,
        role: str,
        content: str
    ) -> Message:

        mensaje = Message(
            conversation_id=conversation_id,
            role=role,
            content=content
        )

        db.add(mensaje)
        db.commit()
        db.refresh(mensaje)

        return mensaje
    
    def obtener_mensajes_por_conversacion(
            self,
            db: Session,
            conversation_id: str
    ) -> list[Message]:
        
        consulta = (
            select(Message)
            .where(Message.conversation_id == conversation_id)
            .order_by(Message.created_at)
        )

        return db.scalars(consulta).all()
    
    def obtener_ultimos_mensajes_por_conversacion(
        self,
        db: Session,
        conversation_id: str,
        limite: int
    ) -> list[Message]:

        consulta = (
            select(Message)
            .where(Message.conversation_id == conversation_id)
            .order_by(desc(Message.created_at))
            .limit(limite)
        )

        mensajes = db.scalars(consulta).all()
        mensajes.reverse()
        return mensajes