# PigBot Backend

Backend del chatbot especializado en porcicultura, desarrollado con Python y FastAPI.

El sistema permite procesar consultas mediante texto y audio, utilizar inteligencia artificial para generar respuestas y mantener información relevante de las conversaciones mediante un sistema de memoria.

## Tecnologías

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- OpenAI API
- Uvicorn

## Funcionalidades

- Chat mediante texto.
- Chat mediante audio.
- Transcripción de audio mediante OpenAI.
- Generación de respuestas mediante inteligencia artificial.
- Persistencia de conversaciones y mensajes.
- Memoria conversacional de corto plazo.
- Memoria permanente mediante resúmenes automáticos.
- Actualización de información relevante de las conversaciones.
- Arquitectura basada en proveedores para el servicio de transcripción.
- Manejo de errores durante la comunicación con los servicios de inteligencia artificial.

## Estructura del proyecto

```text
PigBotBackend/
│
├── app/
│   ├── config/
│   ├── conversation/
│   ├── database/
│   ├── models/
│   ├── prompts/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   │   └── providers/
│   └── main.py
│
├── .env.example
├── .gitignore
└── requirements.txt