from app.config.settings import MEMORY_MESSAGE_LIMIT
from app.services.summary_service import SummaryService
from app.services.message_service import MessageService

class MemoryService:

    def __init__(self):
        self.message_service = MessageService()
        self.summary_service = SummaryService()

    def obtener_contexto(
        self,
        db,
        conversation_id,
        system_prompt
    ):

        resumen = self.obtener_resumen(
            db=db,
            conversation_id=conversation_id
        )

        historial_db = self.obtener_historial(
            db=db,
            conversation_id=conversation_id
        )

        contexto = self.construir_contexto(
            system_prompt=system_prompt,
            resumen=resumen,
            historial_db=historial_db
        )

        return contexto
    
    def obtener_system_prompt(
        self,
        system_prompt
    ):
        
        return [
            {
                "role": "system",
                "content": system_prompt
            }
        ]
    
    def obtener_historial(
        self,
        db,
        conversation_id
    ):

        return self.message_service.obtener_ultimos_mensajes_por_conversacion(
            db=db,
            conversation_id=conversation_id,
            limite=MEMORY_MESSAGE_LIMIT
        )
    
    def construir_contexto(
        self,
        system_prompt,
        resumen,
        historial_db
    ):

        contexto = self.obtener_system_prompt(
            system_prompt=system_prompt
        )

        if resumen:
            contexto.append(
                {
                    "role": "system",
                    "content": (
                        "Esta es la memoria permanente de la conversación. "
                        "Utiliza esta información para responder cuando sea relevante. "
                        "Si existe un conflicto entre esta memoria y los mensajes recientes, "
                        "prioriza la información más reciente.\n\n"
                        f"{resumen}"
                    )
                }
            )

        for mensaje in historial_db:
            contexto.append(
                {
                    "role": mensaje.role,
                    "content": mensaje.content
                }
            )
        return contexto
    
    def obtener_resumen(
        self,
        db,
        conversation_id
    ):

        return self.summary_service.obtener_o_crear_resumen(
            db=db,
            conversation_id=conversation_id
        ).summary