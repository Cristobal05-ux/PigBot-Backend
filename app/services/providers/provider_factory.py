from app.config import settings

from app.services.providers.openai_provider import OpenAIProvider
from app.services.providers.transcription_provider import (
    TranscriptionProvider,
)


def get_transcription_provider() -> TranscriptionProvider:
    """
    Devuelve una instancia del proveedor de transcripción configurado.
    """

    providers = {
        "openai": OpenAIProvider,
    }

    provider = providers.get(settings.TRANSCRIPTION_PROVIDER)

    if provider is None:
        raise ValueError(
            f"Proveedor de transcripción '{settings.TRANSCRIPTION_PROVIDER}' no soportado."
        )

    return provider()