import logging

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.audio_service import AudioService
from app.services.chat_service import ChatService
from app.services.dependencies import (
    get_audio_service,
    get_chat_service,
)


logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_texto(
    datos: ChatRequest,
    db: Session = Depends(get_db),
    chat_service: ChatService = Depends(get_chat_service),
):
    """
    Recibe un mensaje desde Flutter,
    lo procesa con OpenAI y devuelve la respuesta.
    """

    if not datos.mensaje or not datos.mensaje.strip():
        raise HTTPException(
            status_code=400,
            detail="El mensaje no puede estar vacío."
        )

    try:

        respuesta = chat_service.responder(
            db=db,
            mensaje=datos.mensaje
        )

        return ChatResponse(
            respuesta=respuesta
        )

    except RuntimeError as e:

        logger.exception(
            "Error procesando mensaje de texto"
        )

        raise HTTPException(
            status_code=502,
            detail=str(e)
        )


@router.post("/chat/audio", response_model=ChatResponse)
async def chat_audio(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    audio_service: AudioService = Depends(get_audio_service),
    chat_service: ChatService = Depends(get_chat_service),
):
    """
    Recibe un archivo de audio, lo transcribe
    y procesa el texto con el chatbot.
    """

    if (
        not file.content_type
        or not file.content_type.startswith("audio/")
    ):
        raise HTTPException(
            status_code=400,
            detail="El archivo debe ser un formato de audio válido."
        )

    try:

        texto = audio_service.transcribir(file)

        respuesta = chat_service.responder(
            db=db,
            mensaje=texto
        )

        return ChatResponse(
            respuesta=respuesta
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except RuntimeError as e:

        logger.exception(
            "Error procesando audio"
        )

        raise HTTPException(
            status_code=502,
            detail=str(e)
        )