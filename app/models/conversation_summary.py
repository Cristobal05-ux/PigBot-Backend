from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ConversationSummary(Base):
    __tablename__ = "conversation_summaries"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    conversation_id: Mapped[str] = mapped_column(
        ForeignKey("conversations.id"),
        unique=True
    )

    summary: Mapped[str] = mapped_column(
        Text,
        default=""
    )

    conversation = relationship(
        "Conversation",
        back_populates="summary"
    )