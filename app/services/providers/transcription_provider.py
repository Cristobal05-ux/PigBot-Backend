from abc import ABC, abstractmethod

class TranscriptionProvider(ABC):
    """
    Interfaz base para cualquier proveedor de transcripción.
    """

    @abstractmethod
    def transcribir(self, archivo) -> str:
        """
        Transcribe un archivo de audio y devuelve el texto.
        """
        pass