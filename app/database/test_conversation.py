from app.database.database import SessionLocal
from app.models.conversation import Conversation
from app.models.message import Message
from app.services.conversation_service import ConversationService

db = SessionLocal()

service = ConversationService()

conversacion = service.crear_conversacion(db)

print("Conversación creada:")
print(conversacion.id)

db.close()