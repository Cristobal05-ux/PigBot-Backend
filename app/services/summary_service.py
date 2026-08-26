from sqlalchemy import select, func
from app.models.message import Message
from sqlalchemy.orm import Session

from app.models.conversation_summary import ConversationSummary

class SummaryService:

    def obtener_resumen(
        self,
        db: Session,
        conversation_id: str
    ):

        consulta = select(ConversationSummary).where(
            ConversationSummary.conversation_id == conversation_id
        )

        return db.scalar(consulta)

    def crear_resumen(
        self,
        db: Session,
        conversation_id: str
    ):

        resumen = ConversationSummary(
            conversation_id=conversation_id,
            summary=""
        )

        db.add(resumen)
        db.commit()
        db.refresh(resumen)

        return resumen
    
    def obtener_o_crear_resumen(
        self,
        db: Session,
        conversation_id: str
    ):

        resumen = self.obtener_resumen(
            db=db,
            conversation_id=conversation_id
        )

        if resumen is None:
            resumen = self.crear_resumen(
                db=db,
                conversation_id=conversation_id
            )

        return resumen
    
    def actualizar_resumen(
        self,
        db: Session,
        resumen: ConversationSummary,
        nuevo_resumen: str
    ):

        resumen.summary = nuevo_resumen
        db.commit()
        db.refresh(resumen)

        return resumen
    
    def contar_mensajes(
        self,
        db: Session,
        conversation_id: str
    ):

        consulta = (
            select(
                func.count(Message.id)
            )
            .where(
                Message.conversation_id == conversation_id
            )
        )

        return db.scalar(consulta)