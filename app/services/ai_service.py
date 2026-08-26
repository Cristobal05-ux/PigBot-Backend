import logging
import os

from dotenv import load_dotenv
from openai import OpenAI

from app.config.settings import (
    OPENAI_MODEL,
    TEMPERATURE,
    MAX_TOKENS,
)

from app.prompts.pigbot_prompt import PIGBOT_SYSTEM_PROMPT
from app.prompts.summary_prompt import SUMMARY_SYSTEM_PROMPT


logger = logging.getLogger(__name__)

load_dotenv()


class AIService:

    def __init__(self):

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "No se encontró la variable OPENAI_API_KEY en el archivo .env"
            )

        self.client = OpenAI(api_key=api_key)
        self.system_prompt = PIGBOT_SYSTEM_PROMPT

    def generar_respuesta(
        self,
        mensaje: str
    ):

        mensajes = [
            {
                "role": "system",
                "content": self.system_prompt,
            },
            {
                "role": "user",
                "content": mensaje,
            },
        ]

        return self._generar_chat(mensajes)

    def generar_respuesta_con_historial(
        self,
        historial: list
    ):

        return self._generar_chat(historial)

    def generar_resumen(
        self,
        resumen_actual: str,
        historial: list
    ):

        mensajes = [
            {
                "role": "system",
                "content": SUMMARY_SYSTEM_PROMPT
            }
        ]

        if resumen_actual:
            mensajes.append(
                {
                    "role": "system",
                    "content": (
                        "Este es el resumen acumulado hasta ahora. "
                        "Consérvalo y actualízalo únicamente con la información nueva:\n\n"
                        f"{resumen_actual}"
                    )
                }
            )

        mensajes.extend(historial)

        return self._generar_chat(mensajes)

    def _generar_chat(
        self,
        messages: list
    ):

        try:

            respuesta = self.client.chat.completions.create(
                model=OPENAI_MODEL,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
                messages=messages,
            )

            return respuesta.choices[0].message.content

        except Exception as e:

            logger.exception("Error al comunicarse con OpenAI")

            raise RuntimeError(
                "No fue posible comunicarse con el servicio de inteligencia artificial."
            ) from e