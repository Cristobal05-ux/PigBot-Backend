from app.services.providers.provider_factory import (
    get_transcription_provider,
)


class AudioService:

    def __init__(self):
        self.provider = get_transcription_provider()

    def transcribir(self, archivo) -> str:
        return self.provider.transcribir(archivo)