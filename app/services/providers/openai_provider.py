import logging

from fastapi import UploadFile
from openai import OpenAI

from app.config import settings
from app.services.providers.transcription_provider import (
    TranscriptionProvider,
)


logger = logging.getLogger(__name__)


class OpenAIProvider(TranscriptionProvider):

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def transcribir(
        self,
        archivo: UploadFile
    ) -> str:

        try:

            archivo.file.seek(0)

            respuesta = self.client.audio.transcriptions.create(
                model="gpt-4o-mini-transcribe",
                file=(
                    archivo.filename,
                    archivo.file,
                    archivo.content_type
                ),
            )

            texto = respuesta.text.strip()

            if not texto:
                raise ValueError(
                    "No se pudo obtener texto del audio."
                )

            return texto

        except ValueError:
            raise

        except Exception as e:

            logger.exception(
                "Error al transcribir el audio con OpenAI"
            )

            raise RuntimeError(
                "No fue posible transcribir el audio."
            ) from e