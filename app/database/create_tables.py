from app.database.base import Base
from app.database.database import engine
from app.models.conversation_summary import ConversationSummary

# Importar modelos para que SQLAlchemy los registre
from app.models.conversation import Conversation
from app.models.message import Message

print("Creando tablas...")

Base.metadata.create_all(bind=engine)

print("Tablas creadas correctamente.")