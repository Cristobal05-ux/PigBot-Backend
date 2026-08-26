from app.database.database import SessionLocal

# Registrar modelos
import app.models

from app.services.conversation_service import ConversationService
from app.services.message_service import MessageService

db = SessionLocal()

conversation_service = ConversationService()
message_service = MessageService()

conversacion = conversation_service.crear_conversacion(db)

mensaje = message_service.guardar_mensaje(
    db=db,
    conversation_id=conversacion.id,
    role="user",
    content="Hola PigBot"
)

print("Conversación:", conversacion.id)
print("Mensaje:", mensaje.id)

db.close()