import logging

from sqlalchemy.orm import Session

from app.config.settings import SUMMARY_TRIGGER_MESSAGES
from app.services.ai_service import AIService
from app.services.conversation_service import ConversationService
from app.services.memory_service import MemoryService
from app.services.message_service import MessageService
from app.services.summary_service import SummaryService


logger = logging.getLogger(__name__)


class ChatService:

    def __init__(self):
        self.ai = AIService()
        self.conversation_service = ConversationService()
        self.message_service = MessageService()
        self.memory_service = MemoryService()
        self.summary_service = SummaryService()

    def responder(
        self,
        db: Session,
        mensaje: str
    ):

        conversacion = self.conversation_service.obtener_o_crear_conversacion(
            db
        )

        self.message_service.guardar_mensaje(
            db=db,
            conversation_id=conversacion.id,
            role="user",
            content=mensaje
        )

        historial = self.memory_service.obtener_contexto(
            db=db,
            conversation_id=conversacion.id,
            system_prompt=self.ai.system_prompt
        )

        respuesta = self.ai.generar_respuesta_con_historial(
            historial
        )

        self.message_service.guardar_mensaje(
            db=db,
            conversation_id=conversacion.id,
            role="assistant",
            content=respuesta
        )

        if self._debe_actualizar_resumen(
            db=db,
            conversation_id=conversacion.id
        ):

            try:

                self._actualizar_resumen(
                    db=db,
                    conversation_id=conversacion.id
                )

            except Exception:

                logger.exception(
                    "Error al actualizar el resumen de la conversación"
                )

        return respuesta

    def _debe_actualizar_resumen(
        self,
        db: Session,
        conversation_id: str
    ):

        cantidad = self.summary_service.contar_mensajes(
            db=db,
            conversation_id=conversation_id
        )

        return (
            cantidad > 0
            and cantidad % SUMMARY_TRIGGER_MESSAGES == 0
        )

    def _actualizar_resumen(
        self,
        db: Session,
        conversation_id: str
    ):

        resumen = self.summary_service.obtener_o_crear_resumen(
            db=db,
            conversation_id=conversation_id
        )

        mensajes = self.message_service.obtener_ultimos_mensajes_por_conversacion(
            db=db,
            conversation_id=conversation_id,
            limite=SUMMARY_TRIGGER_MESSAGES
        )

        historial = [
            {
                "role": mensaje.role,
                "content": mensaje.content
            }
            for mensaje in mensajes
        ]

        nuevo_resumen = self.ai.generar_resumen(
            resumen_actual=resumen.summary,
            historial=historial
        )

        self.summary_service.actualizar_resumen(
            db=db,
            resumen=resumen,
            nuevo_resumen=nuevo_resumen
        )