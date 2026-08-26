import os

from dotenv import load_dotenv

load_dotenv()

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4.1-mini"

# Generación
TEMPERATURE = 0.6
MAX_TOKENS = 500

# Memoria y resumen
MEMORY_MESSAGE_LIMIT = 3
SUMMARY_TRIGGER_MESSAGES = 20

# Audio
TRANSCRIPTION_PROVIDER = "openai"